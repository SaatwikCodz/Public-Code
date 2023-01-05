from customtkinter import *

set_appearance_mode('dark')
set_default_color_theme('blue')

Start = CTk()
Start.title("Discounter")
label1 = CTkLabel(Start, text = "Welcome to this online Discounter Project", font = ("Times", 36)).pack()
btn1 = CTkButton(Start, text = "Login",fg_color="transparent",text_color=("gray10", "#DCE4EE"),border_width = 2, border_color = "cyan",height = 52, width = 123,corner_radius = 13).place(x = 583, y = 304)
btn1 = CTkButton(Start, text = "Signup",fg_color="transparent",text_color=("gray10", "#DCE4EE"),border_width = 2, border_color = "cyan",height = 52, width = 123,corner_radius = 13).place(x = 583, y = 374)
Start.attributes('-fullscreen', True)
Start.mainloop()