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
————————————————
版权声明：本文为CSDN博主「超自然祈祷」的原创文章，遵循CC
4.0
BY - SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https: // blog.csdn.net / sinat_27382047 / java / article / details / 80161637
'''