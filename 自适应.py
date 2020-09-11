# 布局自定义尺寸
from tkinter import *


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack(fill=BOTH, expand=1)
        listbox = Listbox(frame)  # listbox=Listbox(frame,height=3,selectmode=BROWSE) #curselection()
        for item in ['red', 'green', 'blue', 'yellow', 'pink']:
            listbox.insert(END, item)
        listbox.grid(row=0, column=0, sticky=W + E + N + S)  # sticky 适配
        text = Text(frame, relief=SUNKEN)
        text.grid(row=0, column=1, sticky=W + E + N + S)
        text.insert(END, 'word' * 1000)
        frame.columnconfigure(1, weight=1)  # 尺寸适配
        frame.rowconfigure(0, weight=1)  # 尺寸适配

        # Spinbox(frame,values=('a','b','c')).grid(row=3) #get()


root = Tk()
root.wm_title('尺寸适配')
app = App(root)
root.geometry("400x300+0+0")  # 尺寸适配
root.mainloop()