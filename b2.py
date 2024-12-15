import sqlite3
# Kết nối tới cơ sở dữ liệu trong bộ nhớ
conn = sqlite3.connect("example.db")
cursor = conn.cursor()
conn.close()
