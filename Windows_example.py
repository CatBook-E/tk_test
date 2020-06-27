from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title('Windosw Example')
        # Style().theme_use('TFrame', background='#FFAA34')
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        lb1 = Label(self, text='Windows')
        lb1.grid(sticky=W, pady=4, padx=5)

        area = Text(self)
        area.grid(row=1, column=0, columnspan=2,
                  rowspan=4, padx=5, sticky=E + W + S + N)

        abtun = Button(self, text='Active')
        abtun.grid(row=1, column=3)

        cbtun = Button(self, text='Close')
        cbtun.grid(row=2, column=3, pady=4)

        hbutn = Button(self, text='Help')
        hbutn.grid(row=5, column=0, padx=5)

        obutn = Button(self, text='OK')
        obutn.grid(row=5, column=3)


def main():

    root = Tk()
    root.geometry('350x300+300+300')
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
