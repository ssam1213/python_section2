from Tkinter import *

def printHello() :
    print('Hi')

root = Tk()

w = Label(root, text="Python test")
b = Button(root, text="Click", command=printHello)
c = Button(root, text="Quit", command=root.quit)

w.pack()
b.pack()
c.pack()

root.mainloop() 