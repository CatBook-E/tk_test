from tkinter import *
from tkinter import ttk


def trefun(event):
    sels = event.widget.selection()  # event.widget获取Treeview对象，调用selection获取选择对象名称
    for idx in sels:
        print(tv.item(idx)["text"])
    print("111")


if __name__ == '__main__':
    # global tv
    # _dex = dex("classes.dex")
    # _strs = _dex.getStrings()

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