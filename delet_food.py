import tkinter as tk

def add_and_multiply():
    current_text = text.get("1.0", tk.END).strip()  # الحصول على النص الحالي
    numbers = current_text.split()  # تقسيم النص إلى أرقام باستخدام الفاصل الافتراضي (المسافة)
    result = 1
    for num_str in numbers:
        num = int(num_str)  # تحويل النص إلى عدد صحيح
        result *= num  # ضرب الأرقام معًا
    text.delete("1.0", tk.END)  # حذف النص الحالي في Textbox
    text.insert("1.0", str(result))  # إدراج النتيجة في Textbox

root = tk.Tk()

text = tk.Text(root)
text.pack()

add_button = tk.Button(root, text="Add and Multiply", command=add_and_multiply)
add_button.pack()

root.mainloop()