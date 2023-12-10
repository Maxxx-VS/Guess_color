import tkinter as Tk
from PIL import Image
from PIL import ImageColor
import random

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

def choice_1():
    global t

    root = Tk.Tk()
    root.title("УГАДАЙ ЦВЕТ")
    root.geometry("1366x768")
    root.resizable(width=True, height=True)
    root.iconbitmap(default="forrst.ico")
    btn1 = Tk.Button(root, width=45, height=10, bg=generator_color(rgb)).place(x=100, y=250)
    btn2 = Tk.Button(root, width=45, height=10, bg=generator_color(rgb)).place(x=900, y=250)
    label_1 = Tk.Label(root, text=f"УГАДАЙ ЭТОТ {color} ЦВЕТ", bg='cadet blue', font='Arial 30').pack()

def choice_2():
    root = Tk.Tk()
    root.title("УГАДАЙ ЦВЕТ")
    root.geometry("1366x768")
    root.resizable(width=True, height=True)
    root.iconbitmap(default="forrst.ico")
    btn1 = Tk.Button(root, width=45, height=10, bg=generator_color(rgb)).place(x=100, y=250)
    btn2 = Tk.Button(root, width=45, height=10, bg=generator_color(rgb)).place(x=900, y=250)
    btn3 = Tk.Button(root, width=45, height=10, bg=generator_color(rgb)).place(x=100, y=450)
    btn4 = Tk.Button(root, width=45, height=10, bg=generator_color(rgb)).place(x=900, y=450)
    label_2 = Tk.Label(root, text=f"УГАДАЙ ЭТОТ {color} ЦВЕТ", bg='cadet blue', font='Arial 30').pack()

def choice_3():
    root = Tk.Tk()
    root.title("УГАДАЙ ЦВЕТ")
    root.geometry("1366x768")
    root.resizable(width=True, height=True)
    root.iconbitmap(default="forrst.ico")
    btn1 = Tk.Button(root, width=45, height=10, bg=generator_color(rgb)).place(x=100, y=250)
    btn2 = Tk.Button(root, width=45, height=10, bg=generator_color(rgb)).place(x=500, y=250)
    btn3 = Tk.Button(root, width=45, height=10, bg=generator_color(rgb)).place(x=900, y=250)
    btn4 = Tk.Button(root, width=45, height=10, bg=generator_color(rgb)).place(x=100, y=450)
    btn5 = Tk.Button(root, width=45, height=10, bg=generator_color(rgb)).place(x=500, y=450)
    btn6 = Tk.Button(root, width=45, height=10, bg=generator_color(rgb)).place(x=900, y=450)
    label_3 = Tk.Label(root, text=f"УГАДАЙ ЭТОТ {color} ЦВЕТ", bg='cadet blue', font='Arial 30').pack()

def guess():
    window = Tk.Tk()
    window.title("УГАДАЙ ЦВЕТ")
    window.geometry("1250x400")
    window.resizable(width=True, height=True)
    window.iconbitmap(default="forrst.ico")

    label_name = Tk.Label(window, text="ИГРА УГАДАЙ ЦВЕТ КВАДРТА", bg='cadet blue', font='Arial 30').pack()
    label_level = Tk.Label(window, text="ВЫБИРАЙ УРОВЕНЬ СЛОЖНОСИ: ", font='Arial 18').place(x=75, y=100)

    btn_easy = Tk.Button(window, text='EASY', font='Arial 14', width=20, height=2, bg='#CCFFCC',
                          activebackground='black', command=choice_1).place(x=150, y=175)

    btn_middle = Tk.Button(window, text='MIDDLE', font='Arial 14', width=20, height=2, bg='#00ff00',
                          activebackground='black', command=choice_2).place(x=550, y=175)

    btn_hard = Tk.Button(window, text='HARD', font='Arial 14', width=20, height=2, bg='#00944C',
                          activebackground='black', command=choice_3).place(x=950, y=175)
    window.mainloop()

guess()


