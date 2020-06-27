from tkinter import Tk, BOTH, Listbox, StringVar, END
from tkinter.ttk import Frame, Label


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Listbox")

        self.pack(fill=BOTH, expand=1)

        acts = ['Monkey', 'Tiger', 'Dog',
                'Rabbit', 'Dark', 'House']
        box = Listbox(self)
        for i in acts:
            box.insert(END, i)

        box.bind('<<Animal>>', self.onSelect)

        box.pack(pady=15)
        
