from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Treeview表格数据')

columns = ['1', '2', '3', '4', '5']
tree = ttk.Treeview(root, column=columns, height=20,
                    show='headings'
                    )
tree.pack()

tree.heading('1', text='学号')
tree.heading('2', text='姓名')
tree.heading('3', text='性别')
tree.heading('4', text='成绩')
tree.heading('5', text='名次')

tree.column('1', width=100, anchor='center')
tree.column('2', width=100, anchor='center')
tree.column('3', width=100, anchor='center')
tree.column('4', width=100, anchor='center')
tree.column('5', width=100, anchor='center')

Z = ['0001', '赵一', '男', '658', '1']
Q = ['0002', '钱二', '男', '648', '2']
S = ['0003', '孙三', '女', '638', '3']
L = ['0004', '李四', '女', '628', '4']

number = ['001', '002', '003', '004']
name = ['赵一', '钱二', '孙三', '李四']
gender = ['男', '男', '女', '女']
score = ['658', '648', '638', '628']
rank = ['1', '2', '3', '4']

'''
函数语法
range(start, stop[, step])
参数说明：
start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
'''
for i in range(min(len(number), len(name), len(gender), len(name), len(name))):  # 写入数据
    tree.insert('', i, values=(number[i], name[i], gender[i], score[i], rank[i]))
'''
#排序部分1：
def treeviewrank(tv, col, reverse):  # Treeview、列名、排列方式
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)  # 排序方式
    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):  # 根据排序后索引移动
        tv.move(k, '', index)
    tv.heading(col, command=lambda: treeviewrank(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题
'''


def set_itemvalue(event):
    for item in tree.selection():
        item_text = tree.item(item, "values")
        print(item, item_text)
    # 确定编辑的行、列
    column = tree.identify_column(event.x)  # 列
    row = tree.identify_row(event.y)  # 行
    print(column, row)
    cn = int(str(column).replace('#', ''))  # 列
    rn = int(str(row).replace('I', ''))  # 行
    print(cn, rn)
    # Entry创建摆放
    entryedit = Text(root, width=14, height=1)
    entryedit.place(x=0 + (cn - 1) * 100, y=6 + rn * 20)

    # treevview值=entry值
    def saveedit():
        tree.set(item, column=column, value=entryedit.get(0.0, "end"))
        entryedit.destroy()
        okb.destroy()

    # 按钮创建摆放
    okb = Button(root, text='OK', command=saveedit)
    okb.place(x=90 + (cn - 1) * 100, y=3 + rn * 20)


tree.bind('<Double-1>', set_itemvalue)


def newrow():
    number.append('number')
    name.append('name')
    gender.append('gender')
    score.append('score')
    rank.append('rank')
    tree.insert('', len(number) - 1, values=(number[len(number) - 1], name[len(name) - 1],
                                             gender[len(gender) - 1], score[len(score) - 1], rank[len(rank) - 1]))
    tree.update()
    newb.place(x=200, y=(len(number) - 1) * 20 + 45)
    newb.update()


newb = Button(root, text='新建', width=10, command=newrow)
newb.place(x=200, y=(len(number) - 1) * 20 + 45)
'''
#排序部分2：
for col in columns:  # 绑定函数，使表头可排序
    tree.heading(col, text=col, command=lambda _col=col: treeviewrank(tree, _col, False))
'''


def delcontent():
    items = tree.get_children()
    for item in items:
        tree.delete(item)


Button(root, text='删除列表内容', command=delcontent).pack()


def showcontent(event):
    for num in tree.selection():
        numname = tree.item(num, "values")
    from tkinter import messagebox
    messagebox.showinfo(title=None, message=numname[1])


tree.bind('<ButtonRelease-1>', showcontent)
'''附加1：
# 1.遍历表格
t = treeview.get_children()
for i in t:
    print(treeview.item(i,'values'))
# 2.绑定单击离开事件
def treeviewClick(event):  # 单击
    for item in tree.selection():
        item_text = tree.item(item, "values")
        print(item_text[0:2])  # 输出所选行的第一列的值
tree.bind('<ButtonRelease-1>', treeviewClick)  
'''

tree1 = ttk.Treeview(root)
tree1.pack()
# 参数:parent, index, id=None, **kw (父节点，排序，id不能相同，显示出的文本)
subtree1 = tree1.insert("", 0, id="100", text='中国China', values=("1"))  # ""表示父节点是根
tree1.insert(subtree1, 0, id="101", text="中国北京", values=("3"))  # text表示显示出的文本，values是隐藏的值
tree1.insert(subtree1, 1, id="102", text="中国河北", values=("3"))
tree1.insert(subtree1, 2, id="103", text="中国上海", values=("3"))
tree1.insert(subtree1, 3, id="104", text="中国广州", values=("3"))
subtree2 = tree1.insert("", 1, id="200", text="美国USA", values=("4"))
tree1.insert(subtree2, 0, id="201", text="美国加州", values=("5"))

root.mainloop()