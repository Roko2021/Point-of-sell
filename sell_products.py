import tkinter as tk

def button_click():
    print("Button clicked")

# افتح الملف واقرأ السطور
with open("products.txt", "r",encoding='utf-8') as file:
    lines = file.readlines()

# إنشاء نافذة Tkinter
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# إنشاء أزرار بحسب عدد السطور
for line in lines:
    line = line.strip()# إزالة الفراغات الزائدة والأسطر الفارغة
    mohamed,ahmed = line.split(':')
    button = tk.Button(root, text=mohamed, command=button_click)
    button.pack()
    empty = tk.Label(root,text=ahmed)
    empty.pack()
    many = tk.Entry(root)

root.mainloop()