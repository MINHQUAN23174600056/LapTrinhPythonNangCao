import tkinter as tk
from tkinter import messagebox
import sqlite3

# Kết nối với cơ sở dữ liệu SQLite
conn = sqlite3.connect('LAB6\DATA\product.db')
c = conn.cursor()

# Tạo bảng sản phẩm nếu chưa tồn tại
c.execute('''CREATE TABLE IF NOT EXISTS sanpham
             (Id INTEGER PRIMARY KEY, Ten TEXT, Gia REAL)''')
conn.commit()

def them_san_pham():
    ten = nhap_ten.get()
    gia = nhap_gia.get()
    if ten and gia:
        c.execute("INSERT INTO sanpham (Ten, Gia) VALUES (?, ?)", (ten, gia))
        conn.commit()
        nhap_ten.delete(0, tk.END)
        nhap_gia.delete(0, tk.END)
        hien_thi_san_pham()
    else:
        messagebox.showwarning("Lỗi nhập dữ liệu", "Vui lòng nhập cả tên và giá")

def hien_thi_san_pham():
    danh_sach_san_pham.delete(0, tk.END)
    for row in c.execute("SELECT * FROM sanpham"):
        danh_sach_san_pham.insert(tk.END, f"ID: {row[0]}, Tên: {row[1]}, Giá: {row[2]}")

def xoa_san_pham():
    san_pham_duoc_chon = danh_sach_san_pham.curselection()
    if san_pham_duoc_chon:
        ma_san_pham = danh_sach_san_pham.get(san_pham_duoc_chon).split(",")[0].split(":")[1].strip()
        c.execute("DELETE FROM sanpham WHERE Id=?", (ma_san_pham,))
        conn.commit()
        hien_thi_san_pham()
    else:
        messagebox.showwarning("Lỗi chọn sản phẩm", "Vui lòng chọn một sản phẩm để xóa")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Quản lý sản phẩm")

# Tạo các widget
nhan_ten = tk.Label(root, text="Tên sản phẩm")
nhan_ten.grid(row=0, column=0)
nhap_ten = tk.Entry(root)
nhap_ten.grid(row=0, column=1)

nhan_gia = tk.Label(root, text="Giá sản phẩm")
nhan_gia.grid(row=1, column=0)
nhap_gia = tk.Entry(root)
nhap_gia.grid(row=1, column=1)

nut_them = tk.Button(root, text="Thêm sản phẩm", command=them_san_pham)
nut_them.grid(row=2, column=0, columnspan=2)

danh_sach_san_pham = tk.Listbox(root)
danh_sach_san_pham.grid(row=3, column=0, columnspan=2)

nut_xoa = tk.Button(root, text="Xóa sản phẩm", command=xoa_san_pham)
nut_xoa.grid(row=4, column=0, columnspan=2)
hien_thi_san_pham()
# Chạy vòng lặp chính của ứng dụng
root.mainloop()
conn.close()