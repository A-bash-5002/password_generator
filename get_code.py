import customtkinter as tk

from core import *

core = tk.CTk()
core.state('zoomed')
core.title('pass_gnerator')

tk.set_appearance_mode("Dark")
core.title("Get A Code")
tk.set_default_color_theme('green')


data_text = tk.StringVar()


data_entry = tk.CTkEntry(core,font=('Arial',20) )

showing_label = tk.CTkEntry(core,textvariable = data_text ,font=('Arial',20), state='readonly',text_color = 'black')


def get_data() :
    return get_password(data_entry.get(), read_pass_card())

def change_label() :
    data_text.set(get_data())

my_button = tk.CTkButton(core, text = 'send',font=('Arial',20) ,command= change_label)


showing_label.place(x=600, y=250, width= 500, height=50)
data_entry.place(x=600, y=350, width= 300, height=50)
my_button.place(x= 900, y= 350, width = 100, height=50)


core.mainloop()