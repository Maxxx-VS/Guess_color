import tkinter as Tk
import random
from PIL import ImageColor
import matplotlib.pyplot as plt
import random

arr = []
color_1 = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(1)]
color_2 = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(1)]
color_3 = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(1)]
color_4 = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(1)]
color_5 = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(1)]
color_6 = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(1)]

def switch():
    pass

def choice_1():
    global arr
    root = Tk.Tk()
    root.title("УГАДАЙ ЦВЕТ")
    root.geometry("1366x768")
    root.resizable(width=True, height=True)
    Tk.Canvas(root,
              bg=color_1,
              width=250,
              height=250,).place(x=100, y=250)
    Tk.Canvas(root,
              bg=color_2,
              width=250,
              height=250).place(x=900, y=250)
    arr.append(color_1)
    arr.append(color_2)
    random_color = random.choice(arr)

    print(arr)
    print(random_color)
    label = Tk.Label(root, text=f"УГАДАЙ ЭТОТ {random_color} ЦВЕТ", font='Arial 30').pack()
def choice_2():
    global arr
    root = Tk.Tk()
    root.title("УГАДАЙ ЦВЕТ")
    root.geometry("1366x768")
    root.resizable(width=True, height=True)
    Tk.Canvas(root,
              bg=color_1,
              width=250,
              height=250,).place(x=100, y=100)
    Tk.Canvas(root,
              bg=color_2,
              width=250,
              height=250).place(x=900, y=100)
    Tk.Canvas(root,
              bg=color_3,
              width=250,
              height=250,).place(x=100, y=400)
    Tk.Canvas(root,
              bg=color_4,
              width=250,
              height=250).place(x=900, y=400)
    arr.append(color_1)
    arr.append(color_2)
    arr.append(color_3)
    arr.append(color_4)
    random_color = random.choice(arr)
    print(arr)
    print(random_color)
    label = Tk.Label(root, text=f"УГАДАЙ ЭТОТ {random_color} ЦВЕТ", font='Arial 30').pack()
def choice_3():
    global arr
    root = Tk.Tk()
    root.title("УГАДАЙ ЦВЕТ")
    root.geometry("1366x768")
    root.resizable(width=True, height=True)
    Tk.Canvas(root,
              bg=color_1,
              width=250,
              height=250, ).place(x=100, y=100)
    Tk.Canvas(root,
              bg=color_2,
              width=250,
              height=250).place(x=900, y=100)
    Tk.Canvas(root,
              bg=color_3,
              width=250,
              height=250, ).place(x=100, y=400)
    Tk.Canvas(root,
              bg=color_4,
              width=250,
              height=250).place(x=900, y=400)
    Tk.Canvas(root,
              bg=color_5,
              width=250,
              height=250, ).place(x=100, y=400)
    Tk.Canvas(root,
              bg=color_6,
              width=250,
              height=250).place(x=900, y=400)
    arr.append(color_1)
    arr.append(color_2)
    arr.append(color_3)
    arr.append(color_4)
    arr.append(color_5)
    arr.append(color_6)
    random_color = random.choice(arr)
    print(arr)
    print(random_color)
    label = Tk.Label(root, text=f"УГАДАЙ ЭТОТ {random_color} ЦВЕТ", font='Arial 30').pack()


def guess():
    window = Tk.Tk()
    window.title("УГАДАЙ ЦВЕТ")
    window.geometry("1250x400")
    window.resizable(width=True, height=True)

    Tk.Label(window, text="ИГРА УГАДАЙ ЦВЕТ КВАДРТА", bg='cadet blue', font='Arial 30').pack()
    Tk.Label(window, text="ВЫБИРАЙ УРОВЕНЬ СЛОЖНОСИ: ", font='Arial 18').place(x=75, y=100)

    Tk.Button(window, text='EASY', font='Arial 14', width=20, height=2, bg='#CCFFCC',
              activebackground='black', command=choice_1).place(x=150, y=175)

    Tk.Button(window, text='MIDDLE', font='Arial 14', width=20, height=2, bg='#00ff00',
              activebackground='black', command=choice_2).place(x=550, y=175)

    Tk.Button(window, text='HARD', font='Arial 14', width=20, height=2, bg='#00944C',
              activebackground='black', command=choice_3).place(x=950, y=175)
    window.mainloop()

guess()