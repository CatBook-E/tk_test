'''6.深入in用法'''
# -*- coding: utf-8 -*-
# 使用in属性来指定放置到的容器是那一个，仅能是其master
from tkinter import *

root = Tk()
# root.geometry('800x600')
# 创建两个Frame用作容器
fm1 = Frame(root, bg='red', width=40, height=40)
fm2 = Frame(root, bg='blue', width=40, height=40)
# 再在fm1中创建一个fm3
fm3 = Frame(fm1, bg='yellow', width=20, height=20)

# 创建一个Label,它的master为fm1
lb1 = Label(fm1, text='hello Place', fg='green')
lb1.place(in_=fm1, relx=-1, rely=-0.5, anchor=CENTER)
# 创建一个Button，它的master为fm1
bt1 = Button(fm1, text='hello Place', fg='red')

# 将bt1放置到fm2中，程序报错
# 去掉下面这条语句就可以使用了，可以看到lb1已经正确的放置到fm1的中心位置了
# bt1.place(in_ = fm2,anchor = W)

# 将上面的语句改为下面，即将bt1放置到其fm1的子组件fm3中，这样也是可以的
bt1.place(in_=fm3, anchor=W)

fm1.pack()
fm2.pack()
fm3.pack()
root.mainloop()

# in不是可以随意指定放置的组件的，如果使用in这个参数这个组件必需满足：是其父容器或父容器的子组件