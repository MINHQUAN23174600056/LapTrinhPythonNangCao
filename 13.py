import tkinter as tk
from tkinter import messagebox

def show_message(title, message):
    messagebox.showinfo(title, message)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Hệ thống bài tập Python nâng cao")
root.geometry("400x300")
# Tạo menu
menu_bar = tk.Menu(root)
chapter_menu = tk.Menu(menu_bar, tearoff=0)
for i in range(1, 10):
    chapter_menu.add_command(label=f"1.{i}", command=lambda i=i: show_message("Thông tin", f"Chương 1.{i}: Nội dung bài tập"))
chapter_menu.add_separator()
chapter_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="Chương 1", menu=chapter_menu)
root.config(menu=menu_bar)
root.mainloop()