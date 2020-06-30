from tkinter import *

root = Tk()
root.geometry('800x600')
lb1 = Label(root, text='hello Place Label', fg='green')
bt1 = Button(root, text='hello Place Button', fg='red')
# 创建一个Label
lb1.place(relx=0.5, rely=0.5, anchor=CENTER)

# 在root同创建一个Button，目的是与bt1相比较
bt2 = Button(root, text='button in root', fg='yellow')
bt2.place(anchor=W)
# 在Label中创建一个Button
bt1.place(in_=lb1, anchor=W)
root.mainloop()
