import tkinter as tk
from tkinter import messagebox

def check_age():
    name = entry_name.get()
    try:
        age = int(entry_age.get())
        if age >= 18:
            messagebox.showinfo("Kết quả", f"Chào {name}! Bạn đã trưởng thành")
        else:
            messagebox.showinfo("Kết quả", f"Chào {name}! Bạn còn nhỏ tuổi")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập tuổi là số nguyên hợp lệ")
# Tạo cửa sổ chính
root = tk.Tk()
root.title("Kiểm tra độ tuổi")
root.geometry("400x200")
# Nhãn và hộp nhập
tk.Label(root, text="Nhập tên của bạn:").pack(pady=5)
entry_name = tk.Entry(root, width=20)
entry_name.pack(pady=5)
tk.Label(root, text="Nhập tuổi của bạn:").pack(pady=5)
entry_age = tk.Entry(root, width=20)
entry_age.pack(pady=5)
# Nút kiểm tra
btn = tk.Button(root, text="Kiểm tra", command=check_age)
btn.pack(pady=10)
root.mainloop()