import tkinter as tk

root = tk.Tk()
root.title("Cửa sổ có nhãn")
root.geometry("400x300")
# Tạo nhãn
label = tk.Label(root, text="Đây là nhãn của bạn!", font=("Arial", 16))
label.pack(pady=20)
root.mainloop()