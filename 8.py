import tkinter as tk
def find_divisors():
    try:
        n = int(entry.get())
        divisors = [str(i) for i in range(1, n + 1) if n % i == 0]
        result_label.config(text="Các ước của N: " + " ".join(divisors))
    except ValueError:
        result_label.config(text="Vui lòng nhập số nguyên hợp lệ")
# Tạo cửa sổ chính
root = tk.Tk()
root.title("Liệt kê các ước của N")
root.geometry("400x200")
# Nhãn và hộp nhập
tk.Label(root, text="Nhập số nguyên N:").pack(pady=5)
entry = tk.Entry(root, width=20)
entry.pack(pady=5)
# Nút và kết quả
btn = tk.Button(root, text="Tìm ước", command=find_divisors)
btn.pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)
root.mainloop()