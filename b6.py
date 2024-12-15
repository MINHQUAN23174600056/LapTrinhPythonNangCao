import sqlite3
conn = sqlite3.connect("example2.db")
cursor = conn.cursor()
# Đếm số bản ghi trong bảng 'employees'
cursor.execute("SELECT COUNT(*) FROM employees;")
count = cursor.fetchone()[0]
print(f"Số bản ghi trong bảng 'employees': {count}")
conn.close()
