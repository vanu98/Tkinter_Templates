from tkinter import *

def show_values():
    print (w1.get(), w2.get())

root = Tk()
w1 = Scale(root, from_=0, to=100, )
w1.pack()
w2 = Scale(root, from_=0, to=200, orient=HORIZONTAL)
w2.pack()
Button(root, text='Volume', command=show_values).pack()


mainloop()