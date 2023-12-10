import tkinter as Tk
from PIL import Image
from PIL import ImageColor
import random

rgb = t = (0, 0, 0)

arr = []
color_1 = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(1)]
color_2 = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(1)]
color_3 = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(1)]
color_4 = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(1)]
color_5 = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(1)]
color_6 = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(1)]

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

def switch(bg):
    hex_color = "".join(bg).lstrip('#')
    rgb_color = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
    if rgb_color == random_color:
        print("YES")
    else:
        print("NO")
    print(bg)


def choice_1():
    global arr
    global random_color
    root = Tk.Tk()
    root.title("УГАДАЙ ЦВЕТ")
    root.geometry("1366x768")
    root.resizable(width=True, height=True)
    root.iconbitmap(default="forrst.ico")
    Tk.Button(root, width=45, height=10, bg=color_1, text=color_1, command=lambda: switch(bg=color_1)).place(x=100, y=250)
    Tk.Button(root, width=45, height=10, bg=color_2, text=color_2, command=lambda: switch(bg=color_2)).place(x=900, y=250)
    c1 = "".join(color_1).lstrip('#')
    c2 = "".join(color_2).lstrip('#')
    c1app = tuple(int(c1[i:i+2], 16) for i in (0, 2, 4))
    c2app = tuple(int(c2[i:i+2], 16) for i in (0, 2, 4))
    arr.append(c1app)
    arr.append(c2app)
    random_color = random.choice(arr)
    Tk.Label(root, text=f"УГАДАЙ ЭТОТ {random_color} ЦВЕТ", font='Arial 30').pack()

def choice_2():
    global arr
    global random_color
    root = Tk.Tk()
    root.title("УГАДАЙ ЦВЕТ")
    root.geometry("1366x768")
    root.resizable(width=True, height=True)
    root.iconbitmap(default="forrst.ico")
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
    Tk.Label(root, text=f"УГАДАЙ ЭТОТ {random_color} ЦВЕТ", font='Arial 30').pack()

def choice_3():
    global arr
    global random_color
    root = Tk.Tk()
    root.title("УГАДАЙ ЦВЕТ")
    root.geometry("1366x768")
    root.resizable(width=True, height=True)
    root.iconbitmap(default="forrst.ico")
    Tk.Button(root, width=45, height=10, bg=color_1, text=color_1, command=lambda: switch(bg=color_1)).place(x=100, y=250)
    Tk.Button(root, width=45, height=10, bg=color_2, text=color_2, command=lambda: switch(bg=color_2)).place(x=900, y=250)
    Tk.Button(root, width=45, height=10, bg=color_3, text=color_3, command=lambda: switch(bg=color_3)).place(x=100, y=550)
    Tk.Button(root, width=45, height=10, bg=color_4, text=color_4, command=lambda: switch(bg=color_4)).place(x=900, y=550)
    Tk.Button(root, width=45, height=10, bg=color_5, text=color_5, command=lambda: switch(bg=color_5)).place(x=100, y=950)
    Tk.Button(root, width=45, height=10, bg=color_6, text=color_6, command=lambda: switch(bg=color_6)).place(x=900, y=950)
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
    Tk.Label(root, text=f"УГАДАЙ ЭТОТ {random_color} ЦВЕТ", font='Arial 30').pack()

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


