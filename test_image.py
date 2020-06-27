from PIL import Image, ImageTk
from tkinter import Tk
from tkinter.ttk import Frame, Label
import sys

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.load_image()
        self.initUI()

    def load_image(self):
        try:
            self.img = Image.open(r'/Users/badboy/Desktop/Texture/dome_normal_1001.jpg')
        except:
            print("Error!")
            sys.exit()

    def initUI(self):
        self.master.title('Image')

        tatras = ImageTk.PhotoImage(self.img)
        label = Label(self, image=tatras)

        label.image = tatras

        label.pack()
        self.pack()

    def get_geometry(self):
        w, h = self.img.size
        self.master.geometry('%dx%d+300+300' % (w, h))


def main():
    root = Tk()
    app = Example()
    app.get_geometry()
    root.mainloop()


if __name__ == '__main__':
    main()

