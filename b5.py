import sqlite3
conn = sqlite3.connect("example2.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    position TEXT NOT NULL
);
""")
print("Bảng 'employees' đã được tạo thành công")
# Chèn bản ghi vào bảng
records = [
    ("A", 30, "Engineer"),
    ("B", 25, "Designer"),
    ("C", 35, "Manager")]
cursor.executemany("""
    INSERT INTO employees (name, age, position)
    VALUES (?, ?, ?);""", records)
print("Đã chèn thành công các bản ghi")
conn.commit()
# Truy vấn và hiển thị tất cả các hàng từ bảng
cursor.execute("SELECT * FROM employees;")
rows = cursor.fetchall()
print("Các bản ghi trong bảng 'employees':")
for row in rows:
    print(row)
conn.close()
