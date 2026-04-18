import customtkinter as ctk
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

# customizing ctk
ctk.set_appearance_mode("dark")

# assets
bg = Image.open(r"E:\CS PROJECT YOHO\EntropyZero\assets\BOOTUP.png")
logo = Image.open(r"E:\CS PROJECT YOHO\EntropyZero\assets\EntropyZero_icon.png")

class Bootup_Screen(ctk.CTkFrame):
    def __init__(self, master, command):
        super().__init__(master, bg_color='transparent')

        # bg label
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        self.bg = ctk.CTkImage(dark_image=bg, size=(screen_w, screen_h))
        self.bg_label = ctk.CTkLabel(master=self, text=' ', image=self.bg)
        self.bg_label.place(relx=0, rely=0, relheight=1, relwidth=1)  

        # switch_button
        self.button=ctk.CTkButton(master=self.bg_label,
                             text = 'CONTINUE>>>',
                             font=('Montserrat Black', 30, 'bold'),
                             text_color='#D6D2C4', 
                             fg_color='#002147',
                             bg_color='#002147',
                             hover_color='#002147',
                             width=250, 
                             height=70,
                             command=lambda : self.button_func(command))
        self.button.place(relx=0.72, rely=0.82)  

    def button_func(self, command):
        self.button.configure(state='disabled')       
        command('login_screen')

