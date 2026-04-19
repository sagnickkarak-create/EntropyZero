import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
import os

Image.MAX_IMAGE_PIXELS = None

# customizing ctk
ctk.set_appearance_mode("dark")

# assets
banner = Image.open(r"E:\CS PROJECT YOHO\EntropyZero\assets\SIGNUP.png")

class Signup_Screen(ctk.CTkFrame):
    def __init__(self, master, command, db):
        super().__init__(master, bg_color='#000000')

        # creating db instance
        self.sql_tunnel = db

        # Banner
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        self.banner_img = ctk.CTkImage(dark_image=banner, size=(w, h))
        self.banner_label = ctk.CTkLabel(self, text="", image=self.banner_img)
        self.banner_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Username 
        self.Username = ctk.StringVar()
        self.Username_EF = ctk.CTkEntry(master=self.banner_label,
                                        textvariable=self.Username,
                                        fg_color='#D8D5DB',
                                        text_color='#1C1C1C',
                                        font=('Montserrat Black', 25, 'bold'))
        self.Username_EF.place(relx=0.25, rely=0.25, relwidth=0.25, relheight=0.083333)
        # place

        # Password
        self.Password = ctk.StringVar()
        self.Password_EF = ctk.CTkEntry(master=self.banner_label,
                                        textvariable=self.Password,
                                        fg_color='#D8D5DB',
                                        text_color='#1C1C1C',
                                        font=('Montserrat Black', 25, 'bold'))
        self.Password_EF.place(relx=0.25, rely=0.4583333, relwidth=0.25, relheight=0.083333)

        # Target
        self.Target_Path = ctk.StringVar()
        self.Target_Path_EF = ctk.CTkEntry(master=self.banner_label,
                                        textvariable=self.Target_Path,
                                        fg_color='#D8D5DB',
                                        text_color='#1C1C1C',
                                        font=('Montserrat Black', 25, 'bold'))
        self.Target_Path_EF.place(relx=0.25, rely=0.666666, relwidth=0.25, relheight=0.083333)
        
        # button
        self.continue_button = ctk.CTkButton(master=self.banner_label,
                                             text='>>>',
                                             font=('Montserrat Black', 50, 'bold'),
                                             fg_color='#D8D5DB', 
                                             text_color='#1C1C1C',
                                             bg_color='#000000',
                                             corner_radius=30,
                                             width=100,
                                             height=100,
                                             command= lambda: self.button_functionality(command))
        self.continue_button.place(relx=0.125, rely=0.833333, relheight=0.0833333, relwidth=0.25)        

    def button_functionality(self, command):

        # to feed to mysql
        username=self.Username.get().strip()
        password=self.Password.get().strip()
        path=self.Target_Path.get().strip()

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

                    # disable the button
                    self.continue_button.configure(state='disabled')

                    # to switch screens
                    command('login_screen')
                
                elif response == 'no' :
                    messagebox.showinfo('EntropyZero', 'Be Cautious This Time')
                
        except Exception as error:

            if '1062' in str(error): # 1062 is the error code for unique constraint
                messagebox.showerror('Error', 'Username already taken')
            
            else:
                messagebox.showerror('Error', f'MySQL error : {error}')
        
        

        
        

