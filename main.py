from customtkinter import *
from PIL import Image
import os

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
		Signup = CTk()
		Signup.title("Signup")
		set_appearance_mode("Dark")
		set_default_color_theme("blue")
		lbl5 = CTkLabel(Signup, text="Username", font = ("Times", 23)).place(x = 566, y = 290)
		lbl6 = CTkLabel(Signup, text="Password", font = ("Times", 23)).place(x = 566, y = 370)		
		entry3 = CTkEntry(master = Signup, placeholder_text = "Username", font = ("Times", 14), width = 354)
		entry3.place(x = 466, y = 330)
		entry1 = CTkEntry(master = Signup, placeholder_text = "Password", font = ("Times", 14), width = 354, show = '*')
		entry1.place(x = 466, y = 410)
		btn1 = CTkButton(Signup, text = "Sign Up",fg_color="transparent",text_color=("gray10", "#DCE4EE"),border_width = 2, border_color = "blue",corner_radius = 12)
		btn1.place(x = 566, y = 450)
		lbl7 = CTkLabel(Signup, text = "Already have an account?",font = ("Times", 14))
		lbl7.place(x = 566, y = 485)
		btn2 = CTkButton(Signup, text = "Login",fg_color="transparent",text_color=("gray10", "#DCE4EE"),border_width = 2, border_color = "blue",corner_radius = 12)
		btn2.place(x = 566, y = 520)
		Signup.attributes('-fullscreen', True)
		Signup.mainloop()

	Start = CTk()
	Start.title("Discounter")
	label1 = CTkLabel(Start, text = "Welcome to this online Discounter Project", font = ("Times", 36)).pack()
	btn1 = CTkButton(Start, text = "Login",fg_color="transparent",text_color=("gray10", "#DCE4EE"),border_width = 2, border_color = "blue",height = 52, width = 123,corner_radius = 13, command = login).place(x = 583, y = 304)
	btn1 = CTkButton(Start, text = "Signup",fg_color="transparent",text_color=("gray10", "#DCE4EE"),border_width = 2, border_color = "blue",height = 52, width = 123,corner_radius = 13, command = signup).place(x = 583, y = 374)
	Start.attributes('-fullscreen', True)
	Start.mainloop()
	pass
start()