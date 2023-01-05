from customtkinter import *
from PIL import Image
import os

i = 0

set_appearance_mode('dark')
set_default_color_theme('blue')

def start():
	def login():
		Start.destroy()
		login = CTk()
		login.attributes('-fullscreen', True)
		login.mainloop()
	def signup():
		Start.destroy()
		signup = CTk()
		signup.attributes('-fullscreen', True)
		signup.mainloop()
	Start = CTk()
	Start.title("Discounter")
	label1 = CTkLabel(Start, text = "Welcome to this online Discounter Project", font = ("Times", 36)).pack()
	btn1 = CTkButton(Start, text = "Login",fg_color="transparent",text_color=("gray10", "#DCE4EE"),border_width = 2, border_color = "blue",height = 52, width = 123,corner_radius = 13, command = login).place(x = 583, y = 304)
	btn1 = CTkButton(Start, text = "Signup",fg_color="transparent",text_color=("gray10", "#DCE4EE"),border_width = 2, border_color = "blue",height = 52, width = 123,corner_radius = 13, command = signup).place(x = 583, y = 374)
	Start.attributes('-fullscreen', True)
	Start.mainloop()
	pass
start()