#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tkinter
from tkinter import *
from tkinter import ttk


class tktree(object):
    def __init__(self, tks):
        self.tks = tks
        self.pidlist = {}

    ##清空位置ID列表
    def clearpidlist(self):
        self.pidlist = {}

    ##创建滚动条模块
    def mkscrollbar(self, tk, x=0, y=0, width=0, height=0, orient=None):
        sc1 = tkinter.Scrollbar(tk, orient=orient)
        sc1.place(x=x, y=y, width=width, height=height)
        return sc1

    ##创建tree表的模块，可以选择格式：tree 或者 headings，以及加载滚动条，添加列，固定控件位置，并返回控件指针
    def mktreeview(self, tk=0, x=0, y=0, width=0, height=0, show='tree', columns=[], yscroll=None, xscroll=None):
        treecol = lambda col: [i[0] for i in col]
        xw = 0
        yh = 0
        tr1 = ttk.Treeview(tk, columns=treecol(columns), show=show)
        for i in columns:
            tr1.column(i[0], width=i[1], anchor='center')
            tr1.heading(i[0], text=i[0])
        if yscroll == 'Y':
            xw = 16
            yscr = self.mkscrollbar(tk, x=x + width - xw, y=y, width=xw, height=height)
            tr1['yscrollcommand'] = yscr.set
            yscr.config(command=tr1.yview)
        else:
            pass
        if xscroll == 'Y':
            yh = 16
            xscr = self.mkscrollbar(tk, x=x, y=y + height - yh, width=width - xw, height=yh, orient=HORIZONTAL)
            tr1['xscrollcommand'] = xscr.set
            xscr.config(command=tr1.xview)
        else:
            pass
        tr1.place(x=x, y=y, width=width - xw, height=height - yh)
        return tr1

    def inserttree(self, objs, trees, pid='', flag=0):
        flags = flag
        if isinstance(objs, dict) is True:
            for i in objs:
                ppid = self.inserttree(i, trees, pid, flag=flags)
                flags = flags + 1
                self.inserttree(objs[i], trees, ppid, flag=0)
        elif isinstance(objs, list) is True or isinstance(objs, tuple) is True or isinstance(objs, set) is True:
            k = 0
            for i in objs:
                self.inserttree(i, trees, pid, flag=k)
                k = k + 1
        else:
            ppid = trees.insert(pid, flags, '%s_%d' % (pid, flags), text=objs)
            self.pidlist[ppid] = objs
            return ppid

    def inserttable(self, objs, trees, pid='', flag=0):
        if isinstance(objs, dict) is True:
            flags = flag
            for i in objs:
                pidd = trees.insert(pid, flags, values=objs[i])
                self.pidlist[pidd] = i
                flags = flags + 1


def printchoose1(event):
    tree1.item(tree1.selection(), values=tree1.selection())


def printchoose2(event):
    print(tree2.index(tree2.selection()))


def doublecell(event):  ##输出鼠标右击位置的内容。
    print(tree2.item(tree2.identify_row(event.y), 'values')[int(tree2.identify_column(event.x).split('#')[1]) - 1])


tkt = Tk()
tkt.geometry('700x800+800+200')
tkt.resizable(width=False, height=False)
mktr = tktree(tkt)

data1 = {'a': 'b', 'c': [1, 2, 3, 4, 5, 6, {7: 8}, {9: 10, 11: [12, 13, 14, 15, 16]}],
         'd': {'e': 'f', 'g': {'h': 'i', 'j': ['k', 'l', 'm', 'n']}}, 'o': ('p', 'q', 'r', 's')}
tree1 = mktr.mktreeview(tkt, x=10, y=10, width=300, height=600, show='tree', columns=[('VALID', 60)], yscroll='Y',
                        xscroll='Y')  ##建立属性表
tree1.bind('<ButtonRelease-1>', printchoose1)  ##单击事件响应
mktr.inserttree(data1, tree1)  ##将数据写入树形表中。
print(mktr.pidlist)  ##依次打印树形表中的各个节点元素的位置ID列表

mktr.clearpidlist()

data2_head = [('IDS', 30), ('NAMES', 100), ('SEX', 30), ('AGE', 30)]
data2_data = {1: ('0001', 'ASDDFASAD', 'F', 30), 2: ('0002', 'DFTTGFSFD', 'M', 30), 3: ('0003', 'JGHDRFDCDXX', 'M', 30),
              4: ('0004', 'DFFGDRFSAD', 'M', 30), 5: ('0005', 'YHBCX', 'M', 30), 6: ('0006', 'DFTTGFSFD', 'F', 30)}
tree2 = mktr.mktreeview(tkt, x=320, y=10, width=300, height=600, columns=data2_head, xscroll='Y',
                        show='headings')  ##建立属性表
tree2.bind('<ButtonRelease-1>', printchoose2)  ##添加左击事件
tree2.bind('<ButtonRelease-3>', doublecell)  ##添加右击事件
mktr.inserttable(data2_data, tree2)
print(mktr.pidlist)

tkt.mainloop()