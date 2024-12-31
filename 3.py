import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
# Tạo nhãn với kiểu chữ đậm
label = tk.Label(root, text="Nhãn với kiểu chữ đậm", font=("Arial", 16, "bold"))
label.pack(pady=20)
root.mainloop()