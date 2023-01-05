from customtkinter import *

set_appearance_mode('dark')
set_default_color_theme('blue')

Login_Window = CTk()
Login_Window.title("Login")
btn3 = CTkButton(Login_Window, text = "Login as admin",fg_color="transparent",text_color=("gray10", "#DCE4EE"),border_width = 2, border_color = "cyan",corner_radius = 12)
btn3.place(x = 566, y = 330)
btn4 = CTkButton(Login_Window, text = "Login as user",fg_color="transparent",text_color=("gray10", "#DCE4EE"),border_width = 2, border_color = "cyan",corner_radius = 12)
btn4.place(x = 566, y = 370)
Login_Window.attributes('-fullscreen', True)
Login_Window.mainloop()