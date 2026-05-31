import customtkinter as ctk
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

# customizing ctk
ctk.set_appearance_mode("dark")

# assets
design = Image.open(r"E:\CS PROJECT YOHO\EntropyZero\assets\side screen.jpeg")

class Sorter_Screen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Log_Box
        self.Log_Box = ctk.CTkTextbox(master=self, fg_color="#024659")
        self.Log_Box.configure(state='disabled')
        self.Log_Box.place(relx=0, rely=0, relwidth=0.5, relheight=1)

        # Banner 
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        self.banner_img = ctk.CTkImage(dark_image=design, size=(w/2, h))
        self.banner_label = ctk.CTkLabel(self, text="", image=self.banner_img)
        self.banner_label.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

        

