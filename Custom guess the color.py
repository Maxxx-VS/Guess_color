import customtkinter as CTk
from PIL import Image
from PIL import ImageColor
import random
from functools import partial

rgb = t = (0, 0, 0)
arr = []

def generator_color(rgb):
    global t
    global arr
    global color
    rgb = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
    t = (0, 0, 0)
    lst = list(t)
    lst[0] = rgb[0]
    lst[1] = rgb[1]
    lst[2] = rgb[2]
    t = tuple(lst)
    arr.append(t)
    color = random.choice(arr)
    return "#%02x%02x%02x" % rgb

def switch():
    pass

    # pass
    # ttt = btn1.cget('text')
    # print(ttt)

    # print(color)
    # print("#%02x%02x%02x" % rgb)
    # global color
    # if color == ImageColor.getcolor(root.cget('bg'), "RGB"):
    #     print("YES")
    # else:
    #     print("NO")

my_font = CTk.CTkFont(family="Helvetica", size=44, weight="bold", slant="italic", underline=True, overstrike=True)

def choice_1():
    root = CTk.CTk()
    root.title("УГАДАЙ ЦВЕТ")
    root.geometry("1366x768")
    root.resizable(width=True, height=True)
    root.iconbitmap(default="forrst.ico")
    btn1 = CTk.CTkButton(root, width=45, height=10, bg=generator_color(rgb), text=root.cget('bg')).place(x=100, y=250)
    btn2 = CTk.CTkButton(root, width=45, height=10, bg=generator_color(rgb), text=root.cget('bg')).place(x=900, y=250)
    label_1 = CTk.CTkLabel(master=root, text=f"УГАДАЙ ЭТОТ {33} ЦВЕТ", bg='cadet blue', font=my_font).pack()

def choice_2():
    root = CTk.CTk()
    root.title("УГАДАЙ ЦВЕТ")
    root.geometry("1366x768")
    root.resizable(width=True, height=True)
    root.iconbitmap(default="forrst.ico")
    btn1 = CTk.CTkButton(root, width=45, height=10, bg=generator_color(rgb)).place(x=100, y=250)
    btn2 = CTk.CTkButton(root, width=45, height=10, bg=generator_color(rgb)).place(x=900, y=250)
    btn3 = CTk.CTkButton(root, width=45, height=10, bg=generator_color(rgb)).place(x=100, y=450)
    btn4 = CTk.CTkButton(root, width=45, height=10, bg=generator_color(rgb)).place(x=900, y=450)
    label_2 = CTk.CTkLabel(root, text=f"УГАДАЙ ЭТОТ {33} ЦВЕТ", bg='cadet blue', font=my_font).pack()

def choice_3():
    root = CTk.CTk()
    root.title("УГАДАЙ ЦВЕТ")
    root.geometry("1366x768")
    root.resizable(width=True, height=True)
    root.iconbitmap(default="forrst.ico")
    btn1 = CTk.CTkButton(root, width=45, height=10, bg=generator_color(rgb)).place(x=100, y=250)
    btn2 = CTk.CTkButton(root, width=45, height=10, bg=generator_color(rgb)).place(x=500, y=250)
    btn3 = CTk.CTkButton(root, width=45, height=10, bg=generator_color(rgb)).place(x=900, y=250)
    btn4 = CTk.CTkButton(root, width=45, height=10, bg=generator_color(rgb)).place(x=100, y=450)
    btn5 = CTk.CTkButton(root, width=45, height=10, bg=generator_color(rgb)).place(x=500, y=450)
    btn6 = CTk.CTkButton(root, width=45, height=10, bg=generator_color(rgb)).place(x=900, y=450)
    label_3 = CTk.CTkLabel(root, text=f"УГАДАЙ ЭТОТ {33} ЦВЕТ", bg='cadet blue', font=my_font).pack()

def guess():
    window = CTk.CTk()
    window.title("УГАДАЙ ЦВЕТ")
    window.geometry("1250x400")
    window.resizable(width=True, height=True)
    window.iconbitmap(default="forrst.ico")

    label_name = CTk.CTkLabel(window, text="ИГРА УГАДАЙ ЦВЕТ КВАДРТА", bg='cadet blue', font=my_font).pack()
    label_level = CTk.CTkLabel(window, text="ВЫБИРАЙ УРОВЕНЬ СЛОЖНОСИ: ", font=my_font).place(x=75, y=100)

    btn_easy = CTk.CTkButton(window, text='EASY', font=my_font, width=20, height=2, bg='#CCFFCC',
                          activebackground='black', command=choice_1).place(x=150, y=175)

    btn_middle = CTk.CTkButton(window, text='MIDDLE', font=my_font, width=20, height=2, bg='#00ff00',
                          activebackground='black', command=choice_2).place(x=550, y=175)

    btn_hard = CTk.CTkButton(window, text='HARD', font=my_font, width=20, height=2, bg='#00944C',
                          activebackground='black', command=choice_3).place(x=950, y=175)
    window.mainloop()

guess()


