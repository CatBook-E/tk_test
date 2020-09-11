from tkinter import *
import tkinter.messagebox as messagebox

''''
def getInput(title, message):
    def return_callback(event):
        print('quit...')
        root.quit()

    def close_callback():
        messagebox.showinfo('message', 'no click...')

    root = Tk(className=title)
    root.wm_attributes('-topmost', 1)
    screenwidth, screenheight = root.maxsize()
    width = 300
    height = 100
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(size)
    root.resizable(0, 0)
    lable = Label(root, height=2)
    lable['text'] = message
    lable.pack()
    entry = Entry(root)
    entry.bind('<Return>', return_callback)
    entry.pack()
    entry.focus_set()
    root.protocol("WM_DELETE_WINDOW", close_callback)
    root.mainloop()
    coot = entry.get()
    root.destroy()
"""
————————————————
版权声明：本文为CSDN博主「劲爆音乐网」的原创文章，遵循CC
4.0
BY - SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https: // blog.csdn.net / t60339 / java / article / details / 82842728
"""

getInput('aaa','1234')
'''
import tkinter
# 导入消息对话框子模块
import tkinter.simpledialog

# 创建主窗口
root = tkinter.Tk()
# 设置窗口大小
root.minsize(300, 300)


# 创建函数
def askage():
    # 获取整型（标题，提示，初始值）
    result = tkinter.simpledialog.askinteger(title='获取信息', prompt='请输入年龄：', initialvalue='18')
    # 打印内容
    print(result)


# 添加按钮
btn = tkinter.Button(root, text='获取年龄', command=askage)
btn.pack()

# 加入消息循环
root.mainloop()