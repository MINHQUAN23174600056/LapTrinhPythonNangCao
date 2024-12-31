import tkinter as tk
from math import gcd

def calculate():
    try:
        m = int(entry_m.get())
        n = int(entry_n.get())
        if function_var.get() == "GCD":
            result = gcd(m, n)
            result_label.config(text=f"GCD({m}, {n}) = {result}")
        elif function_var.get() == "LCM":
            result = abs(m * n) // gcd(m, n)
            result_label.config(text=f"LCM({m}, {n}) = {result}")
    except ValueError:
        result_label.config(text="Vui lòng nhập số nguyên hợp lệ")
# Tạo cửa sổ chính
root = tk.Tk()
root.title("Tính toán GCD và LCM")
root.geometry("400x300")
# Nhập giá trị m và n
tk.Label(root, text="Nhập giá trị m:").pack(pady=5)
entry_m = tk.Entry(root, width=20)
entry_m.pack(pady=5)
tk.Label(root, text="Nhập giá trị n:").pack(pady=5)
entry_n = tk.Entry(root, width=20)
entry_n.pack(pady=5)
# Chọn chức năng
tk.Label(root, text="Chọn chức năng:").pack(pady=5)
function_var = tk.StringVar(value="GCD")
function_menu = tk.OptionMenu(root, function_var, "GCD", "LCM")
function_menu.pack(pady=5)
# Nút tính toán và kết quả
btn = tk.Button(root, text="Tính toán", command=calculate)
btn.pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)
root.mainloop()