**Basic Description :**



its like a auto sorter of files based on the file extensions, it also has a manual sort option where user selects a messy folder feeds it to the application and by the click of a button it gets sorted cleanly, the target folder of the sorter is predefined by the user during sign up, I intend to display timestamps and maintain a record of the previous actions for the user to check out, I will be using Python, MySQL and Tkinter(ttk and ctk) for the project



**Problems and their solutions :**



1. The "Ghost" App (UI Freezing)The Problem: Moving 250 files and talking to MySQL in the same loop as the Tkinter window makes the app stop responding to clicks or movement (the "Receptionist in the Warehouse" scenario).The Solution: Use Threading. The Main Thread handles the UI, while a Background Thread (Worker) handles the heavy lifting of moving files and database entries.



2. The "Thread Collision" (Race Conditions)The Problem: If a user clicks the "Sort" button twice, two separate threads will try to move the same 250 files, causing FileNotFoundError crashes.The Solution: Disable the button (state="disabled") the millisecond it's clicked, and only re-enable it in the .finally block of the worker thread.



3. The "Illegal Touch" (UI Safety)The Problem: Background threads aren't allowed to talk to Tkinter widgets directly. If a thread tries to change a label or progress bar, the app becomes unstable.The Solution: Use .after(). The worker thread sends a "request" to the Main Thread to update the UI safely.



4. The "Bottleneck" (Database Latency)The Problem: Sending 250 individual INSERT commands to MySQL one by one is slow because each one waits for a "Success" signal from the server.The Solution: Use Bulk Inserts. Collect all the file history data into a list during the loop, then use executemany() to dump the whole batch into the DB in one go.



5. The "Dirty Data" (File Overwrites)The Problem: If a file with the same name already exists in the target folder (e.g., two different resume.pdf files), the move might overwrite the old one or crash.The Solution: Add a Duplicate Check. Use os.path.exists() and potentially rename the new file (like resume(1).pdf) before moving it.



6. The "Locked File" (Permission Errors)The Problem: If the teacher has a file open in another program while your script tries to move it, the script will crash.The Solution: Try/Except inside the loop. Wrap the specific move command so if one file fails, the loop just logs the error and moves on to file 



**#2.The "Math" Summary:For your % Completed display:**



 1)Count the total files at the start.

 2)Increment a counter for every file processed.

 3)Calculate $\\text{percent} = (\\text{count} / \\text{total}) \\times 100$.

 4)Send that number to the UI via .after().


# MySQL Schema :

To make your User-Defined paths work, you need these three tables. 
They handle the user's identity, their custom folder "map," and the history of every file they've ever moved.

1. Table: users (The Account)T
his is created during the Sign-Up window. 
It stores the "Baton" (the Target Root) that all the other windows will need.

user_id: (INT, Primary Key, Auto-Increment)
username: (VARCHAR)
password: (VARCHAR) — Keep it hashed for safety.
target_root: (VARCHAR) — The "Base Camp" folder (e.g., D:/MySortedFiles).

2. Table: sorting_rules (The Map)
This is populated during your Set-Up window.
This is where the .mp3 -> Music logic lives.
 
rule_id: (INT, Primary Key, Auto-Increment)
user_id: (INT, Foreign Key) — Links the rule to a specific human.
extension: (VARCHAR) — e.g., .jpg
subfolder_name: (VARCHAR) — e.g., Photos
Logic Note: In your Python code, you will join target_root from the first table with subfolder_name from this table to get the final path for Windows Explorer.

3. Table: file_history (The Receipt)
This is populated every time the user clicks the "Sort" button in the Main App. 
It’s your proof that the app actually worked.

log_id: (INT, Primary Key, Auto-Increment)
user_id: (INT, Foreign Key)
file_name: (VARCHAR) — What was the file called?
old_path: (VARCHAR) — Where did it start (Source)?
new_path: (VARCHAR) — Where did it end up (Target)?
timestamp: (DATETIME) — When did this happen?

How they connect in your "Chain Reaction":

Sign-Up Window: Inserts into users. You grab that user_id.
Set-Up Window: Uses that user_id to insert multiple rows into sorting_rules.
Login Window: Queries users to check the password. If it's a match, it grabs the user_id and the target_root.
Main App: Uses the user_id to pull all the rules from sorting_rules into a Python dictionary. As it moves files, it inserts a "receipt" into file_history.



