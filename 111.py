# # from tkinter import *
# import random
# from PIL import ImageColor
# rgb = t = (0, 0, 0)
#
#
# ws = Tk()
# ws.title('PythonGuides')
# ws.geometry('400x300')
# ws.config(bg='#%0x%0x%0x' % (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)))
# rgb = ImageColor.getcolor(ws.cget('bg'), "RGB")
# label = Label(ws, text=f"{rgb}", bg='cadet blue', font='Arial 30').pack()
# print(rgb)
# ws.mainloop()
#
#
# config=print(ImageColor.getcolor(root.cget('bg'), "RGB"))

# def generator_color(rgb):
#     global t
#     global arr
#     global color
#     rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     lst = list(t)
#     lst[0] = rgb[0]
#     lst[1] = rgb[1]
#     lst[2] = rgb[2]
#     t = tuple(lst)
#     arr.append(t)
#     color = random.choice(arr)
#     return "#%02x%02x%02x" % rgb

h = ['#75EBF0']
h1 = "".join(h).lstrip('#')
print (h1)
print('RGB =', tuple(int(h1[i:i+2], 16) for i in (0, 2, 4)))