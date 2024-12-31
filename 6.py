import tkinter as tk

def reverse_text():
    input_text = entry.get()
    reversed_text = ''.join([input_text[i] for i in range(len(input_text)-1, -1, -1)])
    result_label.config(text=reversed_text)
# Tạo cửa sổ chính
root = tk.Tk()
root.title("Đảo ngược chuỗi")
root.geometry("400x200")
# Nhãn và hộp nhập
tk.Label(root, text="Nhập chuỗi:").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)
# Nút và kết quả
btn = tk.Button(root, text="Đảo ngược", command=reverse_text)
btn.pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)
root.mainloop()