#!/usr/bin/env python3
from tkinter import Tk, Frame, Menu


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title("Simple menu")

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.on_exit)
        menubar.add_cascade(label="File", menu=fileMenu)

    def on_exit(self):
        self.quit()


def main():
    root = Tk()
    root.geometry('350x200+300+300')
    app = Example()
    root.mainloop()

'''

def print_hello():
    print("hello1")


def main():
    root = Tk()
    menubar = Menu(root)
    menubar.add_command(label='冬青',
                        command=print_hello)

    root.config(menu=menubar)
    root.mainloop()
'''

if __name__ == '__main__':
    main()



