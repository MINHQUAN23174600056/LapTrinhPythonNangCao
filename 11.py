import tkinter as tk

def convert_year():
    try:
        year = int(entry.get())
        zodiac = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]
        element = ["Kim", "Thủy", "Hỏa", "Thổ", "Mộc"]
        zodiac_year = zodiac[year % 12]
        element_year = element[(year - 4) % 5]
        result_label.config(text=f"Năm âm lịch: {element_year} {zodiac_year}")
    except ValueError:
        result_label.config(text="Vui lòng nhập năm hợp lệ")
# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chuyển đổi năm dương lịch sang âm lịch")
root.geometry("400x200")
# Nhãn và hộp nhập
tk.Label(root, text="Nhập năm dương lịch:").pack(pady=5)
entry = tk.Entry(root, width=20)
entry.pack(pady=5)
# Nút chuyển đổi và kết quả
btn = tk.Button(root, text="Chuyển đổi", command=convert_year)
btn.pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)
root.mainloop()