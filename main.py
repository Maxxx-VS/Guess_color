### ПРОЕКТ ##########################################################################
import tkinter as tk
import PIL.ImageTk as ImageTk
import random

class Hp:
    def __init__(self, image):
        self.window = tk.Tk()
        # Добавление картинки на задний фон
        self.image_path = "ONE.PNG"
        self.image = ImageTk.PhotoImage(file=self.image_path)
        self.label = tk.Label(self.window, image=self.image)
        self.label.pack()

        self.window.title(" (^._.^) OLD PET  (˃ᆺ˂) ")
        self.window.geometry("1366x768")
        self.window.resizable(width=False, height=False)
        self.window.config(bg="grey")
        self.lbl = tk.Label(self.window,
                            bg='grey',
                            text='ЗДЕСЬ  ТЫ  СМОЖЕШЬ  УЗНАТЬ\n СКОЛЬКО  ЧЕЛОВЕЧЕСКИХ  ЛЕТ  ТВОЕМУ  ДОМАШНЕМУ  ЖИВОТНОМУ',
                            font='Arial 24').place(x=110, y=0)

    def win_1(self):
        global answer
        self.root = tk.Toplevel(self.window)
        self.root.title("YOUR CAT'S AGE")
        self.root.geometry("500x500")
        self.root.config(bg="cadet blue")
        self.root.resizable(width=False, height=False)
        self.lbl0 = tk.Label(self.root,
                             bg='cadet blue',
                             font='Arial 16',
                             text='ВВЕДИ ВОЗРАСТ СВОЕГО ЖВОТНОГО').place(x=75, y=50)
        self.btn0 = tk.Button(self.root, text='ПЕРЕСЧИТАТЬ ВОЗРАСТ',
                             font='Arial 14',
                             width=26,
                             height=2,
                             bg='red',
                             activebackground='blue',
                             command=self.valid_1).pack(expand=True)
        self.o = tk.StringVar()
        self.answer = 0
        self.entry = tk.Entry(self.root,
                            textvariable=self.o).place(x=200, y=100)
        # Добавление картинки на задний фон
        self.image_path1 = "CAT.PNG"
        self.image1 = ImageTk.PhotoImage(file=self.image_path1)
        self.label = tk.Label(self.root, image=self.image1)
        self.label.place(x=175, y=350)

    def valid_1(self):
        self.enter = int(self.o.get())
        if self.enter <= 0:
            self.lbl = tk.Label(self.root,
                        bg='cadet blue',
                        font='Arial 26',
                        text=f'ВАША КОШКА\n ЕЩЕ НЕ РОДИЛАСЬ').place(relx=0.5, rely=0.5, anchor="center")
        elif self.enter > 18:
            self.lbl = tk.Label(self.root,
                        bg='cadet blue',
                        font='Arial 26',
                        text=f'СТОЛЬКО КОШКИ\n НЕ ЖИВУТ!').place(relx=0.5, rely=0.5, anchor="center")
        else:
            self.lbl = tk.Label(self.root,
                        bg='cadet blue',
                        font='Arial 26',
                        text=f'ВОЗРАСТ\n ВАШЕЙ КОШКИ =\n {round(self.enter * 4.7, 1)} ЧЕЛОВЕЧЕСКИХ ЛЕТ').place(relx=0.5,
                                                                                                             rely=0.5,
                                                                                                             anchor="center")

    def win_2(self):
        global answer
        self.root = tk.Toplevel(self.window)
        self.root.title("YOUR DOG'S AGE")
        self.root.geometry("500x500")
        # self.bard = Image.open(file="D:\Pet.jpg")
        # self.bardejov = ImageTk.PhotoImage(bard)
        self.root.config(bg="cadet blue")
        self.root.resizable(width=False, height=False)
        self.lbl0 = tk.Label(self.root,
                             bg='cadet blue',
                             font='Arial 16',
                             text='ВВЕДИ ВОЗРАСТ СВОЕГО ЖВОТНОГО').place(x=75, y=50)
        self.btn0 = tk.Button(self.root, text='ПЕРЕСЧИТАТЬ ВОЗРАСТ',
                              font='Arial 14',
                              width=26,
                              height=2,
                              bg='red',
                              activebackground='blue',
                              command=self.valid_2).pack(expand=True)
        self.o = tk.StringVar()
        self.answer = 0
        self.entry = tk.Entry(self.root,
                              textvariable=self.o).place(x=200, y=100)

        self.image_path1 = "DOG.PNG"
        self.image1 = ImageTk.PhotoImage(file=self.image_path1)
        self.label = tk.Label(self.root, image=self.image1)
        self.label.place(x=175, y=350)

    def valid_2(self):
        self.enter = int(self.o.get())
        if self.enter <= 0:
            self.lbl = tk.Label(self.root,
                        bg='cadet blue',
                        font='Arial 26',
                        text=f'ВАША СОБАКА\n ЕЩЕ НЕ РОДИЛАСЬ').place(relx=0.5, rely=0.5, anchor="center")
        elif self.enter > 15:
            self.lbl = tk.Label(self.root,
                        bg='cadet blue',
                        font='Arial 26',
                        text=f'СТОЛЬКО СОБАКИ\n НЕ ЖИВУТ!').place(relx=0.5, rely=0.5, anchor="center")
        else:
            self.lbl = tk.Label(self.root,
                        bg='cadet blue',
                        font='Arial 26',
                        text=f'ВОЗРАСТ\n ВАШЕЙ СОБАКИ =\n {round(self.enter * 6.3, 1)} ЧЕЛОВЕЧЕСКИХ ЛЕТ').place(relx=0.5,
                                                                                                              rely=0.5,
                                                                                                              anchor="center")

    def win_3(self):
        global answer
        self.root = tk.Toplevel(self.window)
        self.root.title("YOUR PARROT'S AGE")
        self.root.geometry("500x500")
        # self.bard = Image.open(file="D:\Pet.jpg")
        # self.bardejov = ImageTk.PhotoImage(bard)
        self.root.config(bg="cadet blue")
        self.root.resizable(width=False, height=False)
        self.lbl0 = tk.Label(self.root,
                             bg='cadet blue',
                             font='Arial 16',
                             text='ВВЕДИ ВОЗРАСТ СВОЕГО ЖВОТНОГО').place(x=75, y=50)
        self.btn0 = tk.Button(self.root, text='ПЕРЕСЧИТАТЬ ВОЗРАСТ',
                              font='Arial 14',
                              width=26,
                              height=2,
                              bg='red',
                              activebackground='blue',
                              command=self.valid_3).pack(expand=True)
        self.o = tk.StringVar()
        self.answer = 0
        self.entry = tk.Entry(self.root,
                              textvariable=self.o).place(x=200, y=100)

        self.image_path1 = "PAR.PNG"
        self.image1 = ImageTk.PhotoImage(file=self.image_path1)
        self.label = tk.Label(self.root, image=self.image1)
        self.label.place(x=175, y=350)

    def valid_3(self):
        self.enter = int(self.o.get())
        if self.enter <= 0:
            self.lbl = tk.Label(self.root,
                        bg='cadet blue',
                        font='Arial 26',
                        text=f'ВАШ ПОПУГАЙ\n ЕЩЕ НЕ РОДИЛСЯ').place(relx=0.5, rely=0.5, anchor="center")
        elif self.enter > 45:
            self.lbl = tk.Label(self.root,
                        bg='cadet blue',
                        font='Arial 26',
                        text=f'СТОЛЬКО ПОПУГАИ\n НЕ ЖИВУТ!').place(relx=0.5, rely=0.5, anchor="center")
        else:
            self.lbl = tk.Label(self.root,
                        bg='cadet blue',
                        font='Arial 26',
                        text=f'ВОЗРАСТ\n ВАШЕГО ПОПУГАЯ =\n {round(self.enter * 1.6, 1)} ЧЕЛОВЕЧЕСКИХ ЛЕТ').place(relx=0.5,
                                                                                                              rely=0.5,
                                                                                                              anchor="center")

    def win_4(self):
        global answer
        self.root = tk.Toplevel(self.window)
        self.root.title("YOUR TORTOISE'S AGE")
        self.root.geometry("500x500")
        # self.bard = Image.open(file="D:\Pet.jpg")
        # self.bardejov = ImageTk.PhotoImage(bard)
        self.root.config(bg="cadet blue")
        self.root.resizable(width=False, height=False)
        self.lbl0 = tk.Label(self.root,
                             bg='cadet blue',
                             font='Arial 16',
                             text='ВВЕДИ ВОЗРАСТ СВОЕГО ЖВОТНОГО').place(x=75, y=50)
        self.btn0 = tk.Button(self.root, text='ПЕРЕСЧИТАТЬ ВОЗРАСТ',
                              font='Arial 14',
                              width=26,
                              height=2,
                              bg='red',
                              activebackground='blue',
                              command=self.valid_4).pack(expand=True)
        self.o = tk.StringVar()
        self.answer = 0
        self.entry = tk.Entry(self.root,
                              textvariable=self.o).place(x=200, y=100)

        self.image_path1 = "TOR.PNG"
        self.image1 = ImageTk.PhotoImage(file=self.image_path1)
        self.label = tk.Label(self.root, image=self.image1)
        self.label.place(x=175, y=350)

    def valid_4(self):
        self.enter = int(self.o.get())
        if self.enter <= 0:
            self.lbl = tk.Label(self.root,
                        bg='cadet blue',
                        font='Arial 26',
                        text=f'ВАША ЧЕРЕПАХА\n ЕЩЕ НЕ РОДИЛСЯ').place(relx=0.5, rely=0.5, anchor="center")
        elif self.enter > 80:
            self.lbl = tk.Label(self.root,
                        bg='cadet blue',
                        font='Arial 26',
                        text=f'СТОЛЬКО ЧЕРЕПАХИ\n НЕ ЖИВУТ!').place(relx=0.5, rely=0.5, anchor="center")
        else:
            self.lbl = tk.Label(self.root,
                        bg='cadet blue',
                        font='Arial 26',
                        text=f'ВОЗРАСТ\n ВАШЕЙ ЧЕРЕПАХИ =\n {round(self.enter * 3.6, 1)} ЧЕЛОВЕЧЕСКИХ ЛЕТ').place(relx=0.5,
                                                                                                              rely=0.5,
                                                                                                              anchor="center")

    def win_5(self):
        global answer
        self.root = tk.Toplevel(self.window)
        self.root.title("YOUR HAMSTER'S AGE")
        self.root.geometry("500x500")
        # self.bard = Image.open(file="D:\Pet.jpg")
        # self.bardejov = ImageTk.PhotoImage(bard)
        self.root.config(bg="cadet blue")
        self.root.resizable(width=False, height=False)
        self.lbl0 = tk.Label(self.root,
                             bg='cadet blue',
                             font='Arial 16',
                             text='ВВЕДИ ВОЗРАСТ СВОЕГО ЖВОТНОГО').place(x=75, y=50)
        self.btn0 = tk.Button(self.root, text='ПЕРЕСЧИТАТЬ ВОЗРАСТ',
                              font='Arial 14',
                              width=26,
                              height=2,
                              bg='red',
                              activebackground='blue',
                              command=self.valid_5).pack(expand=True)
        self.o = tk.StringVar()
        self.answer = 0
        self.entry = tk.Entry(self.root,
                              textvariable=self.o).place(x=200, y=100)

        self.image_path1 = "HAM.PNG"
        self.image1 = ImageTk.PhotoImage(file=self.image_path1)
        self.label = tk.Label(self.root, image=self.image1)
        self.label.place(x=175, y=350)

    def valid_5(self):
        self.enter = int(self.o.get())
        if self.enter <= 0:
            self.lbl = tk.Label(self.root,
                        bg='cadet blue',
                        font='Arial 26',
                        text=f'ВАШ ХОМЯК\n ЕЩЕ НЕ РОДИЛСЯ').place(relx=0.5, rely=0.5, anchor="center")
        elif self.enter > 3:
            self.lbl = tk.Label(self.root,
                        bg='cadet blue',
                        font='Arial 26',
                        text=f'СТОЛЬКО ХОМЯКИ\n НЕ ЖИВУТ!').place(relx=0.5, rely=0.5, anchor="center")
        else:
            self.lbl = tk.Label(self.root,
                        bg='cadet blue',
                        font='Arial 26',
                        text=f'ВОЗРАСТ\n ВАШЕГО ХОМЯКА =\n {round(self.enter * 29.2, 1)} ЧЕЛОВЕЧЕСКИХ ЛЕТ').place(relx=0.5,
                                                                                                              rely=0.5,
                                                                                                              anchor="center")
    def win_6(self):
        global answer
        self.root = tk.Toplevel(self.window)
        self.root.title("YOUR RACCOON'S AGE")
        self.root.geometry("500x500")
        # self.bard = Image.open(file="D:\Pet.jpg")
        # self.bardejov = ImageTk.PhotoImage(bard)
        self.root.config(bg="cadet blue")
        self.root.resizable(width=False, height=False)
        self.lbl0 = tk.Label(self.root,
                             bg='cadet blue',
                             font='Arial 16',
                             text='ВВЕДИ ВОЗРАСТ СВОЕГО ЖВОТНОГО').place(x=75, y=50)
        self.btn0 = tk.Button(self.root, text='ПЕРЕСЧИТАТЬ ВОЗРАСТ',
                              font='Arial 14',
                              width=26,
                              height=2,
                              bg='red',
                              activebackground='blue',
                              command=self.valid_6).pack(expand=True)
        self.o = tk.StringVar()
        self.answer = 0
        self.entry = tk.Entry(self.root,
                              textvariable=self.o).place(x=200, y=100)

        self.image_path1 = "RAC.PNG"
        self.image1 = ImageTk.PhotoImage(file=self.image_path1)
        self.label = tk.Label(self.root, image=self.image1)
        self.label.place(x=175, y=350)

    def valid_6(self):
        self.enter = int(self.o.get())
        if self.enter <= 0:
            self.lbl = tk.Label(self.root,
                        bg='cadet blue',
                        font='Arial 26',
                        text=f'ВАШ ЕНОТ\n ЕЩЕ НЕ РОДИЛСЯ').place(relx=0.5, rely=0.5, anchor="center")
        elif self.enter > 55:
            self.lbl = tk.Label(self.root,
                        bg='cadet blue',
                        font='Arial 26',
                        text=f'СТОЛЬКО ЕНОТЫ\n НЕ ЖИВУТ!').place(relx=0.5, rely=0.5, anchor="center")
        else:
            self.lbl = tk.Label(self.root,
                        bg='cadet blue',
                        font='Arial 26',
                        text=f'ВОЗРАСТ\n ВАШЕГО ЕНОТА =\n {round(self.enter * 20.8, 1)} ЧЕЛОВЕЧЕСКИХ ЛЕТ').place(relx=0.5,
                                                                                                              rely=0.5,
                                                                                                              anchor="center")

    def run(self):
        self.btn1 = tk.Button(self.window, text='CAT', font='Arial 14', width=30, height=2, bg='pink', activebackground='yellow',
                             command=self.win_1).place(x=50, y=175)
        self.btn2 = tk.Button(self.window, text='DOG', font='Arial 14',  width=30, height=2, bg='pink', activebackground='yellow',
                              command=self.win_2).place(x=500, y=175)
        self.btn3 = tk.Button(self.window, text='PARROT', font='Arial 14', width=30, height=2, bg='pink', activebackground='yellow',
                              command=self.win_3).place(x=975, y=175)
        self.btn4 = tk.Button(self.window, text='TORTOISE', font='Arial 14',  width=30, height=2, bg='pink', activebackground='yellow',
                              command=self.win_4).place(x=50, y=300)
        self.btn5 = tk.Button(self.window, text='HAMSTER', font='Arial 14',  width=30, height=2, bg='pink', activebackground='yellow',
                              command=self.win_5).place(x=500, y=300)
        self.btn6 = tk.Button(self.window, text='RACCOON', font='Arial 14',  width=30, height=2, bg='pink', activebackground='yellow',
                              command=self.win_6).place(x=975, y=300)
        self.window.mainloop()
start = Hp('CAT1.png')
start.run()
