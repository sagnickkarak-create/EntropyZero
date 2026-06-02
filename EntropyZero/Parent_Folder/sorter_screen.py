import customtkinter as ctk
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

# customizing ctk
ctk.set_appearance_mode("dark")

# assets
design = Image.open(r"E:\CS PROJECT YOHO\EntropyZero\assets\Gradient Waves.jpg")

class Sorter_Screen(ctk.CTkFrame):
    def __init__(self, master, callback_trigger):
        super().__init__(master)
        self.start_moving = callback_trigger

        # Log_Box
        self.Log_Box = ctk.CTkTextbox(master=self, fg_color="#000000", text_color="#FFB173", font=('Montserrat Black', 10, 'bold'))
        self.Log_Box.configure(state='disabled')
        self.Log_Box.place(relx=0, rely=0, relwidth=0.5, relheight=1)

        # Banner 
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        self.banner_img = ctk.CTkImage(dark_image=design, size=(w/2, h))
        self.banner_label = ctk.CTkLabel(self, text="", image=self.banner_img)
        self.banner_label.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

        # Sort_button
        sort_button = ctk.CTkButton(self, 
                                    fg_color="#065B98", 
                                    text_color="#EFDFBB", 
                                    text="START SORT", 
                                    font=('Montserrat Black', 25, 'bold'),
                                    command=self.start_moving)
        sort_button.place(relx=0.625, rely=0.33333, relwidth=0.25, relheight=0.3)

    def log(self, file, destination):
        message = f"✔ SUCCESS : {file} moved to {destination}"
        self.Log_Box.configure(state='normal')
        self.Log_Box.insert("end", message+'\n')
        self.Log_Box.see("end")
        self.Log_Box.configure(state='disabled')