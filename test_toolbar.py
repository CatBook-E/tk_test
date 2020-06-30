from PIL import Image, ImageTk
from tkinter import Tk, Frame, Menu, Button
from tkinter import LEFT, TOP, X, FLAT, RAISED

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.init_UI()

    def init_UI(self):
        self.master.title('Tool')

        menu_bar = Menu(self.master)
        self.file_menu = Menu(self.master, tearoff=0)
        self.file_menu.add_command(label='Exit', command=self.quit())
        menu_bar.add_cascade(label='File', menu=self.file_menu)

        tool_bar = Frame(self.master, bd=1, relief=RAISED)
        self.img = open(r'../123.jpg')
        eimage = ImageTk.PhotoImage(self.img)

        exit_button = Button(tool_bar, image=eimage, relief=FLAT,
                             command=self.quit)
        exit_button.image = eimage
        exit_button.pack(side=LEFT, padx=2, pady=2)

        tool_bar.pack(side=TOP, fill=X)
        self.master.config(menu=menu_bar)
        self.pack()


def main():
    root = Tk()
    root.geometry('250x150+300+300')
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()