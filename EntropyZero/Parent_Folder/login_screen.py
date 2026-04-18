import customtkinter as ctk
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
from tkinter import messagebox

# customizing ctk
ctk.set_appearance_mode("dark")

# assets
banner = Image.open(r"E:\CS PROJECT YOHO\EntropyZero\assets\LOGIN.png")

class Login_Screen(ctk.CTkFrame):
    def __init__(self, master, switch_command, database_instance):
        super().__init__(master, bg_color='#000000')

        # saving database instance
        self.db = database_instance
        
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
                                             command= lambda: self.continue_button_func(switch_command))
        self.continue_button.place(relx=0.75, rely=0.8, relheight=0.1, relwidth=0.1875)        

    def continue_button_func(self, command): # later add the main screen here as a screen switch and run it in this func
        
        try : 
            # to feed to mysql
            username = self.Username.get().strip()
            password = self.Password.get().strip()

            if username=='' or password=='':
                messagebox.showwarning('Credentials', 'Enter Proper Credentials\n(tip : left anything blank ?)')
            else:
                # check user
                if self.db.check_user(username, password):
                    messagebox.showinfo('EntropyZero', 'Welcome !')

                    # change screen
                    command('sorter_screen')
                else:
                    messagebox.showerror('EntropyZero', 'Invalid Username or Password')

        except Exception as error:
            messagebox.showerror('Error', error)

    def signup_button_func(self, command):
        command('signup_screen')
        self.signup_button.configure(state='disabled')
        

