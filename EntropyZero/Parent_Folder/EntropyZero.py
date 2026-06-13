import customtkinter as ctk
from database import Tunnel
from bootup_screen import Bootup_Screen
from login_screen import Login_Screen
from signup_screen import Signup_Screen
from sorter_screen import Sorter_Screen
from sorter_logic import Logic
from tkinter import messagebox
import os
import threading

# customizing ctk
ctk.set_appearance_mode("dark")

# assets


class EntropyZero(ctk.CTk):
    def __init__(self):
        super().__init__()

        # initializing current user variable
        self.current_user = None

        # creating a db instance
        self.sql_tunnel = Tunnel()

        # rules
        self.after(0, lambda: self.state('zoomed'))
        self.title('EntropyZero')
        # self.resizable(False, False)

        # icon
        self.iconbitmap(os.path.normpath(os.path.join("..", "assets", "EntropyZero_icon._ico.ico")))

        # screens

            # Sorter screen
        self.sorter_screen = Sorter_Screen(self, self.sorter_callback)
        self.sorter_screen.place(relx=0, rely=0, relheight=1, relwidth=1)

            # Signup screen
        self.signup_screen = Signup_Screen(self, self.sql_tunnel, self.handle_signup)
        self.signup_screen.place(relx=0, rely=0, relheight=1, relwidth=1)

            # Login screen
        self.login_screen = Login_Screen(self, self.screen_switch, self.handle_login)
        self.login_screen.place(relx=0, rely=0, relheight=1, relwidth=1)
        
            # Bootup screen
        self.bootup_screen = Bootup_Screen(self, self.screen_switch)
        self.bootup_screen.place(relx=0, rely=0, relheight=1, relwidth=1)

            # Screen dictionary
        self.screens_dict = {'bootup_screen':self.bootup_screen, 'login_screen':self.login_screen, 'signup_screen':self.signup_screen, 'sorter_screen':self.sorter_screen}

        # on closing 
        self.protocol("WM_DELETE_WINDOW", lambda: self.closing_func(self.sql_tunnel))

    def screen_switch(self, screen):
        self.screens_dict[screen].tkraise()

    def closing_func(self, db):
        db.close_connection()
        self.destroy()
    
    def handle_signup(self, username, password, target_path):

        # to feed to mysql
        username=username
        password=password
        path=target_path

        try :

            if username == '' or password == '' or path == '':
                messagebox.showwarning('EntropyZero', 'Enter the required credentials\n(tip : left anything blank ??)')

            if os.path.exists(path) == False :
                messagebox.showerror('Error', 'Given path doesn\'t exist locally')
                
            else :
                response = messagebox.askquestion('Confirm Credentials', f'username : {username}\npassword : {password}\npath : {path}')
                if response == 'yes' :
                    self.sql_tunnel.add_user(username, password, path)
                    messagebox.showinfo('EntropyZero', 'Account Created Successfully !!')

                    # initializing temporary logic instance
                    temp_logic = Logic(path, username)

                    # to create folders
                    temp_logic.info_getter()
                    temp_logic.builder(path)

                    # disable the button
                    self.signup_screen.continue_button.configure(state='disabled')

                    # to switch screens
                    self.screen_switch('login_screen')
                
                elif response == 'no' :
                    messagebox.showinfo('EntropyZero', 'Be Cautious This Time')
                
        except Exception as error:

            if '1062' in str(error): # 1062 is the error code for unique constraint
                messagebox.showerror('Error', 'Username already taken')
            
            else:
                messagebox.showerror('Error', f'MySQL error : {error}')

    def handle_login(self, username, password):

        username = username.strip()
        password = password.strip()

        if username == '' or password == '':
            messagebox.showwarning('Credentials','Enter proper credentials')
        else:
            if self.sql_tunnel.check_user(username, password):
                self.current_user = username
                messagebox.showinfo('EntropyZero',f'Welcome {username}')
                self.path = os.path.normpath(self.sql_tunnel.path_getter(self.current_user))
                self.logic = Logic(self.path, self.current_user)
                self.logic.info_getter()
                self.logic.filename_getter(self.path)
                self.logic.destination_path_builder(self.path)
                self.screen_switch('sorter_screen')
            else:
                messagebox.showerror('EntropyZero','Invalid username or password')

    def sorter_callback(self):
        threading.Thread(target=self.Mover_cum_Log_Updator, daemon=True).start()

    def Mover_cum_Log_Updator(self) :
        
        # initialize the mover 
        mover_results = self.logic.mover(self.path)
        for file, path in mover_results :

            if file=="FAILURE" :
                self.after(10, self.handle_mover_failure, file, path)
            
            else :
                self.after(10, self.sorter_screen.log, file, path)

    def handle_mover_failure(self, file, error_msg) :
        message = f"X FAILURE : {file} not moved, {error_msg}"
        self.sorter_screen.Log_Box.configure(state='normal')
        self.sorter_screen.Log_Box.insert("end", message+'\n')
        self.sorter_screen.Log_Box.see("end")
        self.sorter_screen.Log_Box.configure(state='disabled')
        
EntropyZero().mainloop()