import tkinter
from tkinter import *
from tkinter import messagebox

def delet1():
    
    root1 = Tk()
    root1.title('حذف منتج')
    root1.geometry('300x100')
    user_name = Label(root1,text='اسم المنتج')
    user_name.grid(row=0,column=0)
    user_name_enter = Entry(root1)
    user_name_enter.grid(row=0,column=1)
    pass_word = Label(root1,text='السعر')
    pass_word.grid(row=1,column=0)
    pass_word__enter = Entry(root1)
    pass_word__enter.grid(row=1,column=1)
    def delet():
        def delete_line_with_word(file_path, word):
    # قراءة الملف وحذف السطر
            with open(file_path, 'r',encoding='utf-8') as file:
                lines = file.readlines()

            modified_lines = [line for line in lines if word not in line]

    # حفظ الملف بعد الحذف
            with open(file_path, 'w',encoding='utf-8') as file:
                file.writelines(modified_lines)
            messagebox.showinfo('Deleted','account has beed deleted')

# استخدام الدالة لحذف السطر الذي يحتوي على الكلمة المطلوبة
        file_path = 'products.txt'
        word_to_delete = user_name_enter.get()  # استبدل هذه الكلمة بالتي تريد حذف السطور التي تحتوي عليها
        delete_line_with_word(file_path, word_to_delete)
    
    save1 = Button(root1,text='delet Account',command=delet)
    save1.grid(row=4,column=1)

    root1.mainloop()
delet1()