from tkinter import *
import random
rgb = (0, 0, 0)

def generator_color(rgb):
    rgb = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
    return "#%02x%02x%02x" % rgb





ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg=generator_color(rgb))
ws.mainloop()