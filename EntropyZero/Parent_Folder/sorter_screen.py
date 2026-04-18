import customtkinter as ctk

# customizing ctk
ctk.set_appearance_mode("dark")

class Sorter_Screen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        label = ctk.CTkLabel(master=self, 
                             text='WORK IN PROGRESS !',
                             text_color='#D8D5DB',
                             bg_color='#1C1C1C',
                             font=('Montserrat Black', 100, 'bold'))
        label.place(relx=0, rely=0, relwidth=1, relheight=1)
        