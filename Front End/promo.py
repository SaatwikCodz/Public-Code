from PIL import Image
from customtkinter import *

set_appearance_mode('dark')
set_default_color_theme('blue')

promo = CTk()
e = CTkEntry(promo, placeholder_text = "PROMO CODE HERE")
e.pack()
b = CTkButton(promo, text = "Verify").pack()
promo.mainloop()