import tkinter

# 推出按钮
root = tkinter.Tk()

root.title('Hello world!')
but = tkinter.Button(root, text='quit', width=8, command=root.quit)

but.pack(padx=8, pady=10)
root.geometry("350x250+300+300")

root.mainloop()

