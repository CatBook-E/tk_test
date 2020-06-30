from tkinter import Tk, Frame, Menu


# 右键会产生事件，打开菜单
class Example(Frame):

    def __init__(self):
        super().__init__()

        self.init_UI()

    def init_UI(self):
        self.master.title('Popup Menu')

        self.menu = Menu(self.master, tearoff=0)
        self.menu.add_command(label='Beep', command=self.bell)
        self.menu.add_command(label='Exit', command=self.quit())

        self.master.bind('<Button-3>', self.show_menu)
        self.pack()

    def show_menu(self, e):
        self.menu.post(e.x_root, e.y_root)


def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
