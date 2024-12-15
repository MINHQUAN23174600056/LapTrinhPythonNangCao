import sqlite3
conn = sqlite3.connect("example2.db")
cursor = conn.cursor()
# Cập nhật tất cả các giá trị trong cột 'position' thành 'Updated Position'
cursor.execute("""
UPDATE employees
SET position = 'Updated Position';
""")
print("Cập nhật thành công tất cả các giá trị của cột 'position'.")
conn.commit()
# Truy vấn lại dữ liệu để kiểm tra
cursor.execute("SELECT * FROM employees;")
rows = cursor.fetchall()
print("Các bản ghi sau khi cập nhật:")
for row in rows:
    print(row)
conn.close()
