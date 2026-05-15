import customtkinter as ctk
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
from tkinter import messagebox

# customizing ctk
ctk.set_appearance_mode("dark")

# assets
banner = Image.open(r"E:\CS PROJECT YOHO\EntropyZero\assets\LOGIN.png")

class Login_Screen(ctk.CTkFrame):
    def __init__(self, master, switch_command, login_func):
        super().__init__(master, bg_color='#000000')
        
        # Banner 
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        self.banner_img = ctk.CTkImage(dark_image=banner, size=(w, h))
        self.banner_label = ctk.CTkLabel(self, text="", image=self.banner_img)
        self.banner_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Username Entry Field
        self.Username = ctk.StringVar()
        self.Username_EF = ctk.CTkEntry(master=self.banner_label,
                                        textvariable=self.Username,
                                        fg_color='#D8D5DB',
                                        text_color='#1C1C1C',
                                        font=('Montserrat Black', 25, 'bold'))
        self.Username_EF.place(relx=0.6875, rely=0.3, relheight=0.1, relwidth=0.25)
        
        
        # Password Entry Field
        self.Password = ctk.StringVar()
        self.Password_EF = ctk.CTkEntry(master=self.banner_label,
                                        textvariable=self.Password,
                                        fg_color='#D8D5DB',
                                        text_color='#1C1C1C',
                                        font=('Montserrat Black', 25, 'bold'))
        self.Password_EF.place(relx=0.6875, rely=0.5, relheight=0.1, relwidth=0.25)

        # signup button
        self.signup_button = ctk.CTkButton(master=self.banner_label,
                               text='SIGNUP',
                               font=('Montserrat Black', 50, 'bold'),
                               fg_color="#D8D5DB",
                               text_color='#1C1C1C',
                               bg_color='#000000',
                               corner_radius=30,
                               width=100,
                               height=100,
                               command=lambda: self.signup_button_func(switch_command))
        self.signup_button.place(relx=0.50, rely=0.8, relwidth=0.1875, relheight=0.1)

        # continue button
        self.continue_button = ctk.CTkButton(master=self.banner_label,
                                             text='>>>',
                                             font=('Montserrat Black', 50, 'bold'),
                                             fg_color='#D8D5DB', 
                                             text_color='#1C1C1C',
                                             bg_color='#000000',
                                             corner_radius=30,
                                             width=100,
                                             height=100,
                                             command= lambda: login_func(self.Username.get(), self.Password.get()))
        self.continue_button.place(relx=0.75, rely=0.8, relheight=0.1, relwidth=0.1875)        

    def signup_button_func(self, command):
        command('signup_screen')
        self.signup_button.configure(state='disabled')