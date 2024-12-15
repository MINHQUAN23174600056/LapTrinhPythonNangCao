import sqlite3
conn = sqlite3.connect("example.db")
# Tạo con trỏ
cursor = conn.cursor()
# Tạo bảng
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT
);
""")
print("Bảng 'users' được tạo thành công")
conn.commit()
conn.close()