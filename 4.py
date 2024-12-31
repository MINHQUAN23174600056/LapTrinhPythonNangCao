import tkinter as tk
from tkinter import messagebox

# Hàm xử lý khi nhấn nút Gửi
def submit_info():
    name = entry_name.get()
    student_id = entry_id.get()
    password = entry_password.get()
    messagebox.showinfo("Thông tin đã nhập", f"Tên: {name}\nID Sinh viên: {student_id}\nMật khẩu: {password}")
# Tạo cửa sổ chính
root = tk.Tk()
root.title("Nhập thông tin sinh viên")
root.geometry("400x300")
# Nhãn và hộp nhập cho Tên
tk.Label(root, text="Tên sinh viên:").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)
# Nhãn và hộp nhập cho ID
tk.Label(root, text="ID Sinh viên:").pack(pady=5)
entry_id = tk.Entry(root)
entry_id.pack(pady=5)
# Nhãn và hộp nhập cho Mật khẩu
tk.Label(root, text="Mật khẩu:").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)
# Nút Gửi
btn_submit = tk.Button(root, text="Gửi", command=submit_info)
btn_submit.pack(pady=20)
root.mainloop()