from PIL import Image
from customtkinter import *

set_appearance_mode('dark')
set_default_color_theme('blue')

showroom = CTk()
showroom.title("Showroom")
img = CTkImage(light_image = Image.open("C:/Users/Saatwik Coding/Desktop/GitHub/Public-Code/Images/Item-1.png"),
			   dark_image = Image.open("C:/Users/Saatwik Coding/Desktop/GitHub/Public-Code/Images/Item-1.png"),
			   size = (300, 150)
	)
lbl = CTkLabel(showroom, image = img, text = "").pack()
btn = CTkButton(showroom, text = "Apply Promo", fg_color = "transparent", border_color = "cyan", border_width = 3).pack()
showroom.attributes('-fullscreen', True)
showroom.mainloop()