import sqlite3
conn = sqlite3.connect("example.db")
cursor = conn.cursor()
# Truy vấn danh sách các bảng
cursor.execute("""
SELECT name FROM sqlite_master
WHERE type='table'
ORDER BY name;
""")
# Lấy danh sách các bảng
tables = cursor.fetchall()
print("Danh sách các bảng trong cơ sở dữ liệu:")
for table in tables:
    print(table[0])
conn.close()
