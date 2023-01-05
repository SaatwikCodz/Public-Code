from PIL import Image
from customtkinter import *

set_appearance_mode('dark')
set_default_color_theme('blue')

promo = CTk()
promo.title("Please Enter your CODE")
e = CTkEntry(promo, placeholder_text = "PROMO CODE HERE")
e.pack()
b = CTkButton(promo, text = "Verify", border_color = "cyan", border_width = 3).pack()
promo.attributes('-fullscreen', True)
promo.mainloop()