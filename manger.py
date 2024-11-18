import tkinter
from tkinter import *
import add_seller
import delet_seller
import add_products


root = Tk()
root.geometry('350x70')
root.title('منفذ المدير')

edafet_seller = Button(root,text='اضافه بائع',command=add_seller.add)
edafet_seller.grid(row=1,column=1)
edafet_seller = Button(root,text='حذف بائع',command=delet_seller.delet1)
edafet_seller.grid(row=1,column=3)

space = Label(root,text='              ')
space.grid(row=1,column=2)
space = Label(root,text='              ')
space.grid(row=1,column=0)
space = Label(root,text='              ')
space.grid(row=1,column=4)
space = Label(root,text='              ')
space.grid(row=0,column=4)

edafet_montage = Button(root,text='اضافه منتج',command=add_products.add_product)
edafet_montage.grid(row=1,column=5)

root.mainloop()