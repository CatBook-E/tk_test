from PIL import Image, ImageTk
from tkinter import BOTH, Tk
from tkinter.ttk import Frame, Label, Style

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title('Absolute Posintioning')
        self.pack(fill=BOTH, expand=1)

        # 设置背景颜色
        Style().configure('TFrame', backgroud='#ccc')

        # 我们从当前工作目录中的图像创建图像对象和照片图像对象
        bard = Image.open(r'/Users/badboy/Desktop/Texture/dome_normal_1001.jpg')
        bardejov = ImageTk.PhotoImage(bard)

        label1 = Label(self, image=bardejov)
        # 我们必须保留对图像的引用，以防止图像被垃圾收集。
        label1.image = bardejov
        # 将标签放置在框架上的x = 20和y = 20坐标处。
        label1.place(x=0, y=20)

        bard2 = Image.open(r'/Users/badboy/Desktop/Texture/dome_gloss_1001.jpg')
        img2 = ImageTk.PhotoImage(bard2)
        label2 = Label(self, image=img2)
        label2.image = img2
        label2.place(x=800, y=20)

        bard3 = Image.open(r'/Users/badboy/Desktop/Texture/dome_normal_1001.jpg')
        img3 = ImageTk.PhotoImage(bard3)
        label3 = Label(self, image=img3)
        label3.image = img3
        label3.place(x=20, y=520)


def main():
    root = Tk()
    root.geometry('1000x1000+300+300')
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
