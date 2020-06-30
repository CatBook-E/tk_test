from tkinter import Tk, BOTH, RIGHT, RAISED, LEFT
from tkinter.ttk import Frame, Button, Style


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title('Tkinter pack manager')

        self.style = Style()
        self.style.theme_use('clam')

        # 设置按钮的样式，RAISED为浮雕 borderwidth 是边框宽度
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)

        self.pack(fill=BOTH, expand=True)

        close_button = Button(self, text='close', command=quit)
        close_button.pack(side=RIGHT, padx=5, pady=5)

        ok_button = Button(self, text='OK', command=quit)
        ok_button.pack(side=LEFT, padx=5, pady=5)


def main():
    root = Tk()
    root.geometry('300x250+300+300')
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()