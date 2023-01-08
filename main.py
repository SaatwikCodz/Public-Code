from customtkinter import *
from PIL import Image

set_appearance_mode('dark')
set_default_color_theme('blue')

def login():
	login = CTk()
	login.mainloop()

def start():
	Start = CTk()
	Start.title("Discounter")
	label1 = CTkLabel(Start, text = "Welcome to this online Discounter Project", font = ("Times", 36)).pack()
	btn1 = CTkButton(Start, text = "Login", command = login).place()
	Start.mainloop()

start()