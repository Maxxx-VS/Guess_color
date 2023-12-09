import tkinter as Tk
from PIL import Image
from PIL import ImageColor
import random

rgb = (0, 0, 0)
def generator_color(rgb):
    rgb = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
    return "#%02x%02x%02x" % rgb

def choice_1():
    root = Tk.Tk()
    root.title("УГАДАЙ ЦВЕТ")
    root.geometry("1366x768")
    root.resizable(width=True, height=True)
    root.iconbitmap(default="forrst.ico")
    btn1 = Tk.Button(root, width=45, height=10, bg=generator_color(rgb)).grid(column=0, row=0, padx=50, pady=50)
    btn2 = Tk.Button(root, width=45, height=10, bg=generator_color(rgb)).grid(column=1, row=0, padx=50, pady=50)



def choice_2():
    root = Tk.Tk()
    root.title("УГАДАЙ ЦВЕТ")
    root.geometry("1366x768")
    root.resizable(width=True, height=True)
    root.iconbitmap(default="forrst.ico")
    btn1 = Tk.Button(root, width=45, height=10, bg=generator_color(rgb)).place(x=100, y=140)
    btn2 = Tk.Button(root, width=45, height=10, bg=generator_color(rgb)).place(x=500, y=140)
    btn3 = Tk.Button(root, width=45, height=10, bg=generator_color(rgb)).place(x=900, y=140)
    btn4 = Tk.Button(root, width=45, height=10, bg=generator_color(rgb)).place(x=100, y=350)


def choice_3():
    root = Tk.Tk()
    root.title("УГАДАЙ ЦВЕТ")
    root.geometry("1366x768")
    root.resizable(width=True, height=True)
    root.iconbitmap(default="forrst.ico")
    btn1 = Tk.Button(root, width=45, height=10, bg=generator_color(rgb)).place(x=100, y=290)
    btn2 = Tk.Button(root, width=45, height=10, bg=generator_color(rgb)).place(x=500, y=290)
    btn3 = Tk.Button(root, width=45, height=10, bg=generator_color(rgb)).place(x=900, y=290)
    btn4 = Tk.Button(root, width=45, height=10, bg=generator_color(rgb)).place(x=100, y=500)
    btn5 = Tk.Button(root, width=45, height=10, bg=generator_color(rgb)).place(x=500, y=500)
    btn6 = Tk.Button(root, width=45, height=10, bg=generator_color(rgb)).place(x=900, y=500)






def guess():
    root = Tk.Tk()
    root.title("УГАДАЙ ЦВЕТ")
    root.geometry("1250x400")
    root.resizable(width=True, height=True)
    root.iconbitmap(default="forrst.ico")

    label = Tk.Label(text="ИГРА УГАДАЙ ЦВЕТ КВАДРТА", bg='cadet blue', font='Arial 30').pack()
    label1 = Tk.Label(text="ВЫБИРАЙ УРОВЕНЬ СЛОЖНОСИ: ", font='Arial 18').place(x=75, y=100)

    btn_easy = Tk.Button(root, text='EASY', font='Arial 14', width=20, height=2, bg='#CCFFCC',
                          activebackground='black', command=choice_1).place(x=150, y=175)

    btn_middle = Tk.Button(root, text='MIDDLE', font='Arial 14', width=20, height=2, bg='#00ff00',
                          activebackground='black', command=choice_2).place(x=550, y=175)

    btn_hard = Tk.Button(root, text='HARD', font='Arial 14', width=20, height=2, bg='#00944C',
                          activebackground='black', command=choice_3).place(x=950, y=175)



    root.mainloop()

guess()


