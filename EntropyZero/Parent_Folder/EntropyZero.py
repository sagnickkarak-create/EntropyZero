import customtkinter as ctk
from database import Tunnel
from bootup_screen import Bootup_Screen
from login_screen import Login_Screen
from signup_screen import Signup_Screen
from sorter_screen import Sorter_Screen
from sorter_logic import Logic
from tkinter import messagebox

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
        self.iconbitmap(r"E:\CS PROJECT YOHO\EntropyZero\assets\EntropyZero_icon._ico.ico")

        # screens

            # Sorter screen
        self.sorter_screen = Sorter_Screen(self)
        self.sorter_screen.place(relx=0, rely=0, relheight=1, relwidth=1)

            # Signup screen
        self.signup_screen = Signup_Screen(self, self.screen_switch, self.sql_tunnel)
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
    
    def handle_login(self, username, password):

        username = username.strip()
        password = password.strip()

        if username == '' or password == '':
            messagebox.showwarning('Credentials','Enter proper credentials')
        else:
            if self.sql_tunnel.check_user(username, password):
                self.current_user = username
                messagebox.showinfo('EntropyZero',f'Welcome {username}')
                self.path = self.sql_tunnel.path_getter(self.current_user)
                self.logic = Logic(self.path, self.current_user)
                self.logic.info_getter()
                self.logic.builder(self.path)
                self.screen_switch('sorter_screen')
            else:
                messagebox.showerror('EntropyZero','Invalid username or password')
        
EntropyZero().mainloop()