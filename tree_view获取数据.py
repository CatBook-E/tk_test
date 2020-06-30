'''
import tkinter
from tkinter import ttk  # 导入内部包

li = ['王记', '12', '男']
root = tkinter.Tk()
root.title('测试')
tree = ttk.Treeview(root, columns=['1', '2', '3'], show='headings')
tree.column('1', width=100, anchor='center')
tree.column('2', width=100, anchor='center')
tree.column('3', width=100, anchor='center')
tree.heading('1', text='姓名')
tree.heading('2', text='学号')
tree.heading('3', text='性别')
tree.insert('', 'end', values=li)
tree.grid()


def treeviewClick(event):  # 单击
    print('单击')
    for item in tree.selection():
        item_text = tree.item(item, "values")
        print(item_text[0])  # 输出所选行的第一列的值


tree.bind('<ButtonRelease-1>', treeviewClick)  # 绑定单击离开事件===========

root.mainloop()
'''

from tkinter import *
from tkinter import ttk
"""
bookList = [('aaa', 123), ('bbb', 123), ('xxx', 123), ('sss', 123), ('ddd', 123)]
root = Tk()
frame = ttk.Frame(root)
frame.pack(fill='both', expand='false')
tree = ttk.Treeview(frame, columns=['name', 'price'], show='headings')
tree.heading('name', text='name')
tree.heading('price', text='price')
for item in bookList:
    tree.insert('', 'end', values=item)
tree.pack()

root.mainloop()
"""


def trefun(event):
    sels = event.widget.selection()  # event.widget获取Treeview对象，调用selection获取选择对象名称
    for idx in sels:
        print
        tv.item(idx)["text"]
    print
    "111"


if __name__ == '__main__':
    global tv
    _dex = dex("classes.dex")
    _strs = _dex.getStrings()

    tp = Tk()
    tv = ttk.Treeview(tp)
    tv.grid(row=0, column=0)
    scb = ttk.Scrollbar(tp, command=tv.yview)
    tv.config(yscroll=scb.set)
    scb.grid(row=0, column=1, sticky="ns")
    txt = Text(tp)
    txt.grid(row=0, column=2)
    tv.bind("<<TreeviewSelect>>", trefun)

    rtnode = tv.insert("", 0, "dex", text="dex", values=("1"))
    apknode = tv.insert(rtnode, 1, "apk信息", text="apk信息", values=("1"))
    strsnode = tv.insert(apknode, 2, "strings", text="strings", values=("1"))

    dexclsnode = tv.insert(rtnode, 1, "dexclasses", text="dexclasses", values=("1"))

    strslen = len(_strs)
    for i in range(0, strslen):
        tv.insert(strsnode, -1, strslen - i, text=_strs[i], values=("2"))

    tp.mainloop()