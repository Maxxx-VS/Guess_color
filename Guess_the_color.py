import tkinter as Tk
from PIL import Image
from PIL import ImageColor
import random
import sys
import os

arr = []
color_1 = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(1)]
color_2 = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(1)]
color_3 = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(1)]
color_4 = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(1)]
color_5 = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(1)]
color_6 = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(1)]

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    os.startfile("Guess_the_color.py")

def switch(bg):
    hex_color = "".join(bg).lstrip('#')
    rgb_color = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
    if rgb_color == random_color:
        root = Tk.Tk()
        root.configure(bg=bg)
        root.title("УГАДАЙ ЦВЕТ")
        root.geometry("1366x768")
        Tk.Label(root, bg=bg, text=f"ТЫ УГАДАЛ ЭТОТ: {random_color} ЦВЕТ", font='Arial 30 bold').pack()
        arr.clear()
        Tk.Button(root, width=20, height=2, bg=bg, text="ЗАКОНЧИТЬ ИГРУ", font='Arial 30 bold', command=restart_program).place(relx=0.5, rely=0.5, anchor='center')
        root.resizable(width=True, height=True)
        root.mainloop()
        print("YES")
    else:
        print("NO")

def choice_1():
    global arr
    global random_color
    root = Tk.Tk()
    root.configure(bg="#ebebeb")
    root.title("УГАДАЙ ЦВЕТ")
    root.geometry("1366x768")
    root.resizable(width=True, height=True)
    Tk.Button(root, width=45, height=10, bg=color_1, text=color_1, command=lambda: switch(bg=color_1)).place(x=100, y=250)
    Tk.Button(root, width=45, height=10, bg=color_2, text=color_2, command=lambda: switch(bg=color_2)).place(x=900, y=250)
    c1 = "".join(color_1).lstrip('#')
    c2 = "".join(color_2).lstrip('#')
    c1app = tuple(int(c1[i:i+2], 16) for i in (0, 2, 4))
    c2app = tuple(int(c2[i:i+2], 16) for i in (0, 2, 4))
    arr.append(c1app)
    arr.append(c2app)
    random_color = random.choice(arr)
    Tk.Label(root, bg="#ebebeb", text=f"УГАДАЙ ЭТОТ: {random_color} ЦВЕТ", font='Arial 30 bold').pack()
def choice_2():
    global arr
    global random_color
    root = Tk.Tk()
    root.configure(bg="#ebebeb")
    root.title("УГАДАЙ ЦВЕТ")
    root.geometry("1366x768")
    root.resizable(width=True, height=True)
    Tk.Button(root, width=45, height=10, bg=color_1, text=color_1, command=lambda: switch(bg=color_1)).place(x=100, y=150)
    Tk.Button(root, width=45, height=10, bg=color_2, text=color_2, command=lambda: switch(bg=color_2)).place(x=900, y=150)
    Tk.Button(root, width=45, height=10, bg=color_3, text=color_3, command=lambda: switch(bg=color_3)).place(x=100, y=450)
    Tk.Button(root, width=45, height=10, bg=color_4, text=color_4, command=lambda: switch(bg=color_4)).place(x=900, y=450)
    c1 = "".join(color_1).lstrip('#')
    c2 = "".join(color_2).lstrip('#')
    c3 = "".join(color_1).lstrip('#')
    c4 = "".join(color_2).lstrip('#')
    c1app = tuple(int(c1[i:i+2], 16) for i in (0, 2, 4))
    c2app = tuple(int(c2[i:i+2], 16) for i in (0, 2, 4))
    c3app = tuple(int(c3[i:i+2], 16) for i in (0, 2, 4))
    c4app = tuple(int(c4[i:i+2], 16) for i in (0, 2, 4))
    arr.append(c1app)
    arr.append(c2app)
    arr.append(c3app)
    arr.append(c4app)
    random_color = random.choice(arr)
    Tk.Label(root, bg="#ebebeb", text=f"УГАДАЙ ЭТОТ: {random_color} ЦВЕТ", font='Arial 30 bold').pack()
def choice_3():
    global arr
    global random_color
    root = Tk.Tk()
    root.configure(bg="#ebebeb")
    root.title("УГАДАЙ ЦВЕТ")
    root.geometry("1366x768")
    root.resizable(width=True, height=True)
    Tk.Button(root, width=45, height=10, bg=color_1, text=color_1, command=lambda: switch(bg=color_1)).place(x=100, y=75)
    Tk.Button(root, width=45, height=10, bg=color_2, text=color_2, command=lambda: switch(bg=color_2)).place(x=900, y=75)
    Tk.Button(root, width=45, height=10, bg=color_3, text=color_3, command=lambda: switch(bg=color_3)).place(x=100, y=250)
    Tk.Button(root, width=45, height=10, bg=color_4, text=color_4, command=lambda: switch(bg=color_4)).place(x=900, y=250)
    Tk.Button(root, width=45, height=10, bg=color_5, text=color_5, command=lambda: switch(bg=color_5)).place(x=100, y=425)
    Tk.Button(root, width=45, height=10, bg=color_6, text=color_6, command=lambda: switch(bg=color_6)).place(x=900, y=425)
    c1 = "".join(color_1).lstrip('#')
    c2 = "".join(color_2).lstrip('#')
    c3 = "".join(color_1).lstrip('#')
    c4 = "".join(color_2).lstrip('#')
    c5 = "".join(color_1).lstrip('#')
    c6 = "".join(color_2).lstrip('#')
    c1app = tuple(int(c1[i:i+2], 16) for i in (0, 2, 4))
    c2app = tuple(int(c2[i:i+2], 16) for i in (0, 2, 4))
    c3app = tuple(int(c3[i:i+2], 16) for i in (0, 2, 4))
    c4app = tuple(int(c4[i:i+2], 16) for i in (0, 2, 4))
    c5app = tuple(int(c5[i:i+2], 16) for i in (0, 2, 4))
    c6app = tuple(int(c6[i:i+2], 16) for i in (0, 2, 4))
    arr.append(c1app)
    arr.append(c2app)
    arr.append(c3app)
    arr.append(c4app)
    arr.append(c5app)
    arr.append(c6app)
    random_color = random.choice(arr)
    Tk.Label(root, bg="#ebebeb", text=f"УГАДАЙ ЭТОТ: {random_color} ЦВЕТ", font='Arial 30 bold').pack()
def guess():
    window = Tk.Tk()
    window.configure(bg="#ebebeb")
    window.title("УГАДАЙ ЦВЕТ")
    window.geometry("1300x400")
    window.resizable(width=True, height=True)
    Tk.Label(window, text="ИГРА УГАДАЙ ЦВЕТ КВАДРТА", bg="#ebebeb", font='Arial 30 bold').pack()

    Tk.Button(window, text='EASY', font='Arial 14 bold', width=20, height=2, bg='#CCFFCC',
              activebackground='black', command=choice_1).place(relx=0.1, rely=0.25)
    Tk.Button(window, text='MEDIUM', font='Arial 14 bold', width=20, height=2, bg='#00ff00',
              activebackground='black', command=choice_2).place(relx=0.4, rely=0.25)
    Tk.Button(window, text='HARD', font='Arial 14 bold', width=20, height=2, bg='#00944C',
              activebackground='black', command=choice_3).place(relx=0.7, rely=0.25)
    window.mainloop()
guess()


