import tkinter as tk
from tkinter import messagebox

def calculate_fare():
    try:
        km = float(entry_km.get())
        waiting_time = int(entry_waiting.get())
        if km <= 0.8:
            fare = 12000
        elif km <= 30:
            fare = 12000 + (km - 0.8) * 15300
        else:
            fare = 12000 + (30 - 0.8) * 15300 + (km - 30) * 12100

        # Thêm phí chờ
        if waiting_time > 5:
            fare += (waiting_time - 5) * 750

        result_label.config(text=f"Cước phí: {fare:,.0f} đồng")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số km và thời gian chờ hợp lệ")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Tính cước taxi")
root.geometry("400x300")

# Nhãn và hộp nhập
tk.Label(root, text="Số km đã đi:").pack(pady=5)
entry_km = tk.Entry(root)
entry_km.pack(pady=5)

tk.Label(root, text="Thời gian chờ (phút):").pack(pady=5)
entry_waiting = tk.Entry(root)
entry_waiting.pack(pady=5)

# Nút và kết quả
btn = tk.Button(root, text="Tính cước", command=calculate_fare)
btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Hiển thị cửa sổ
root.mainloop()