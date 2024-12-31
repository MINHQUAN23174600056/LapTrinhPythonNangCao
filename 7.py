import tkinter as tk

def calculate_sum():
    try:
        n = int(entry.get())
        total_sum = sum(range(1, n + 1))
        result_label.config(text=f"Tổng từ 1 đến {n}: {total_sum}")
    except ValueError:
        result_label.config(text="Vui lòng nhập một số nguyên hợp lệ")
# Tạo cửa sổ chính
root = tk.Tk()
root.title("Tính tổng từ 1 đến N")
root.geometry("400x200")
# Nhãn và hộp nhập
tk.Label(root, text="Nhập N:").pack(pady=5)
entry = tk.Entry(root, width=20)
entry.pack(pady=5)
# Nút và kết quả
btn = tk.Button(root, text="Tính tổng", command=calculate_sum)
btn.pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)
root.mainloop()