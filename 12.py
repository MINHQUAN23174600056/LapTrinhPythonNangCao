import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = weight / (height ** 2)
        bmi_label.config(text=f"BMI: {bmi:.2f}")
        if bmi < 18.5:
            result_label.config(text="Kết luận: Gầy")
        elif 18.5 <= bmi < 24.9:
            result_label.config(text="Kết luận: Bình thường")
        elif 25 <= bmi < 29.9:
            result_label.config(text="Kết luận: Thừa cân")
        else:
            result_label.config(text="Kết luận: Béo phì")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập cân nặng và chiều cao hợp lệ")
# Tạo cửa sổ chính
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x200")
# Nhãn và hộp nhập
tk.Label(root, text="Cân nặng (kg):").pack(pady=5)
entry_weight = tk.Entry(root)
entry_weight.pack(pady=5)
tk.Label(root, text="Chiều cao (m):").pack(pady=5)
entry_height = tk.Entry(root)
entry_height.pack(pady=5)
# Nút và kết quả
btn = tk.Button(root, text="Tính BMI", command=calculate_bmi)
btn.pack(pady=10)
bmi_label = tk.Label(root, text="")
bmi_label.pack(pady=5)
result_label = tk.Label(root, text="")
result_label.pack(pady=5)
root.mainloop()