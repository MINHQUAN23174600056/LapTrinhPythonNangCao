import tkinter as tk

def show_image():
    # Tải ảnh định dạng hỗ trợ .gif hoặc .ppm
    img = tk.PhotoImage(file="example.gif")  
    label.config(image=img)
    label.image = img  # Giữ tham chiếu đến ảnh để không bị xóa khỏi bộ nhớ
# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chương trình xem ảnh")
root.geometry("500x400")
# Nút để hiển thị ảnh
btn = tk.Button(root, text="Hiển thị ảnh", command=show_image)
btn.pack(pady=10)
label = tk.Label(root)
label.pack()
root.mainloop()