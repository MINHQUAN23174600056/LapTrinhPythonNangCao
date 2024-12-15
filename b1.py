import sqlite3
# Kết nối tới cơ sở dữ liệu (sẽ tạo mới nếu chưa tồn tại)
conn = sqlite3.connect("example.db")
# Tạo con trỏ
cursor = conn.cursor()
# Lấy và in phiên bản SQLite
cursor.execute("SELECT sqlite_version();")
version = cursor.fetchone()
print("SQLite version:", version[0])
conn.close()