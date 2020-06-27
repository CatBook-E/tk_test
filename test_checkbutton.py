import tkinter
from tkinter import Tk, Frame, Checkbutton
from tkinter import BooleanVar, BOTH

'''
# 检查按钮
def toggle_tittle():
    is_tittle_shown = cbvar.get()
    print(is_tittle_shown)
    if is_tittle_shown:
        root.title('Checkbutton example')
    else:
        root.title('')


root = tkinter.Tk()
cbvar = tkinter.BooleanVar()
toggle_tittle()
# 检查按钮
cbutn = tkinter.Checkbutton(root, text='show', width=8, variable=cbvar, command=toggle_tittle())
cbutn.select()
cbutn.pack(pady=10)
# 退出按钮
but = tkinter.Button(root, text='quit', width=8, command=root.quit)
but.pack(pady=10)
root.geometry("350x200+300+300")
toggle_tittle()
root.mainloop()
'''

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title("Checkbutton")

        self.pack(fill=BOTH, expand=True)
        self.var = BooleanVar()

        cb = Checkbutton(self, text="Show title",
                         variable=self.var, command=self.onClick)
        cb.select()
        cb.place(x=50, y=50)

    def onClick(self):

        if self.var.get() == True:
            self.master.title("Checkbutton")
        else:
            self.master.title("")


def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()