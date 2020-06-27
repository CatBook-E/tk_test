from tkinter import Tk, Frame, Menu


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Submenu")

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        filemenu = Menu(menubar)

        sumenu = Menu(filemenu)
        sumenu.add_command(label='New feed')
        sumenu.add_command(label='Book marks')
        sumenu.add_command(label='mail')
        filemenu.add_cascade(label='Import', menu=sumenu, underline=0)

        filemenu.add_separator()

        filemenu.add_command(label='Exit', underline=0, command=self.quit())
        menubar.add_cascade(label='File', underline=0, menu=filemenu)


def main():
    root = Tk()
    root.geometry("350x250+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()


