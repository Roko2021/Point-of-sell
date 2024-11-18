import tkinter
from tkinter import *
from tkinter import messagebox

def add():
    
    root1 = Tk()
    root1.title('اضافه بائع')
    root1.geometry('300x100')
    user_name = Label(root1,text='User name')
    user_name.grid(row=0,column=0)
    user_name_enter = Entry(root1)
    user_name_enter.grid(row=0,column=1)
    pass_word = Label(root1,text='Password')
    pass_word.grid(row=1,column=0)
    pass_word__enter = Entry(root1,show='*')
    pass_word__enter.grid(row=1,column=1)
    re_password = Label(root1,text='Re Password')
    re_password.grid(row=2,column=0)
    re_password_enter = Entry(root1,show='*')
    re_password_enter.grid(row=2,column=1)
    
    def save():
        if pass_word__enter.get() != re_password_enter.get():
            un_correct = Label(root1,text='un correct',font=('tajawal',8,'bold'))
            un_correct.grid(row=2,column=2)
        else:
            found = False
            try:
                with open('seller.txt','r') as file1:
                    for line in file1:
                        account = line.split(':')
                        user = account[0]
                        if user_name_enter.get() in user:
                            found = True
                            messagebox.showinfo('error','Username has beed taken')
                            break
                            
            except FileNotFoundError:
                pass
            
            if not found:
                with open('seller.txt','a',encoding='utf-8') as file:
                    file.write(f'\n{user_name_enter.get()}:{pass_word__enter.get()}')
                    messagebox.showinfo('saved','the account has been saved')
    
    save1 = Button(root1,text='Save Account',command=save)
    save1.grid(row=4,column=1)


    root1.mainloop()