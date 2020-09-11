"""
@Author : 行初心
@Date   : 18-9-30
@Blog   : www.cnblogs.com/xingchuxin
@Gitee  : gitee.com/zhichengjiu
"""
from tkinter import *


def main():
    root = Tk()
    # tearoff=True
    menubar = Menu(root, tearoff=True)
    menubar.add_command(label='果部')
    menubar.add_command(label='菜部')
    frame = Frame(root,
                  width=100, height=100,
                  background='red')
    frame.pack()

    def _right_key(event):
        menubar.post(event.x_root, event.y_root)

    # frame框绑定鼠标右键
    frame.bind("<Button-3>", _right_key)
    mainloop()


if __name__ == '__main__':
    main()