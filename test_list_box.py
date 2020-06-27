from tkinter import Tk, BOTH, Listbox, StringVar, END
from tkinter.ttk import Frame, Label

# 有 Bug 选择的对象不显示名字
class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Listbox")

        self.pack(fill=BOTH, expand=1)

        acts = ['Monkey', 'Tiger', 'Dog',
                'Rabbit', 'Dark', 'House']
        lb = Listbox(self)
        for i in acts:
            lb.insert(END, i)

        lb.bind("<<Animal>>", self.on_select)

        lb.pack(pady=15)

        self.var = StringVar()
        self.label = Label(self, text=0, textvariable=self.var)
        self.label.pack()

    def on_select(self, val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)

        self.var.set(value)


def main():
    root = Tk()
    app = Example()
    root.geometry('350x200+300+300')

    root.mainloop()


if __name__ == '__main__':
    main()
