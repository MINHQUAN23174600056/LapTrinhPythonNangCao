import sqlite3
conn = sqlite3.connect("example2.db")
cursor = conn.cursor()
# Xóa một hàng cụ thể dựa trên điều kiện
cursor.execute("""
DELETE FROM employees
WHERE name = 'Bob';
""")
print("Đã xóa thành công hàng có tên 'Bob'")
conn.commit()
# Truy vấn lại dữ liệu để kiểm tra
cursor.execute("SELECT * FROM employees;")
rows = cursor.fetchall()
print("Các bản ghi còn lại trong bảng:")
for row in rows:
    print(row)
conn.close()
