import tkinter
from tkinter import *
from tkinter import messagebox

def add_product():
    root = Tk()
    root.geometry('300x100')
    root.title('اضافه منتج')
    name_products = Label(root,text='اسم المنتج')
    name_products.grid(row=0,column=0)
    name_products_enter = Entry(root)
    name_products_enter.grid(row=0,column=1)
    price_product = Label(root,text='سعر المنتج')
    price_product.grid(row=1,column=0)
    price_product_enter = Entry(root)
    price_product_enter.grid(row=1,column=1)
    def products():
        with open('products.txt','a',encoding='utf-8') as file:
            file.write(f'\n{name_products_enter.get()}:{price_product_enter.get()}')
            messagebox.showinfo('success','has success')
    click_save = Button(root,text='اضافه',command=products)
    click_save.grid(row=2,column=1)
    
    
    root.mainloop()
add_product()