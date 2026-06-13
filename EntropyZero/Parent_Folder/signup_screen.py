import customtkinter as ctk
from PIL import Image
import os

Image.MAX_IMAGE_PIXELS = None

# customizing ctk
ctk.set_appearance_mode("dark")

# assets
banner = Image.open(os.path.normpath(os.path.join("..", "assets", "SIGNUP.png")))

class Signup_Screen(ctk.CTkFrame):
    def __init__(self, master, db, handle_signup):
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
                                             command= lambda: handle_signup(self.Username.get(), self.Password.get(), os.path.normpath(self.Target_Path.get())))
        self.continue_button.place(relx=0.125, rely=0.833333, relheight=0.0833333, relwidth=0.25)