import sqlite3
def create_database():
    # Kết nối tới cơ sở dữ liệu (tự động tạo file nếu chưa tồn tại)
    conn = sqlite3.connect("LAB4\DATA\product.db")
    cursor = conn.cursor()
    conn.commit()
    conn.close()

def display_products():
    conn = sqlite3.connect("LAB4\DATA\product.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    print("\nDanh Sách Sản Phẩm:")
    print("ID | Name | Price | Amount")
    for product in products:
        print(f"{product[0]} | {product[1]} | {product[2]} | {product[3]}")
    conn.close()
def add_product():
    name = input("Nhập tên sản phẩm: ")
    price = float(input("Nhập giá sản phẩm: "))
    amount = int(input("Nhập số lượng sản phẩm: "))
    conn = sqlite3.connect("LAB4\DATA\product.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)", (name, price, amount))
    conn.commit()
    conn.close()
    print("Thêm sản phẩm thành công!\n")

def search_product():
    name = input("Nhập tên sản phẩm cần tìm: ")
    conn = sqlite3.connect("LAB4\DATA\product.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product WHERE Name LIKE ?", (f"%{name}%",))
    products = cursor.fetchall()
    print("\nKết Quả Tìm Kiếm:")
    if products:
        print("ID | Name | Price | Amount")
        for product in products:
            print(f"{product[0]} | {product[1]} | {product[2]} | {product[3]}")
    else:
        print("Không tìm thấy sản phẩm phù hợp.")
    conn.close()

def update_product():
    product_id = int(input("Nhập ID sản phẩm cần cập nhật: "))
    new_price = float(input("Nhập giá mới: "))
    new_amount = int(input("Nhập số lượng mới: "))
    conn = sqlite3.connect("LAB4\DATA\product.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE product SET Price = ?, Amount = ? WHERE Id = ?", (new_price, new_amount, product_id))
    conn.commit()
    conn.close()
    print("Cập nhật sản phẩm thành công!\n")

def delete_product():
    product_id = int(input("Nhập ID sản phẩm cần xóa: "))
    conn = sqlite3.connect("LAB4\DATA\product.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM product WHERE Id = ?", (product_id,))
    conn.commit()
    conn.close()
    print("Xóa sản phẩm thành công!\n")

def main_menu():
    while True:
        print("\n--- Quản Lý Sản Phẩm ---")
        print("1. Hiển Thị Danh Sách Sản Phẩm")
        print("2. Thêm Sản Phẩm Mới")
        print("3. Tìm Kiếm Sản Phẩm Theo Tên")
        print("4. Cập Nhật Thông Tin Sản Phẩm")
        print("5. Xóa Sản Phẩm")
        print("6. Thoát")
        choice = input("Chọn chức năng (1-6): ")
        if choice == "1":
            display_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_product()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại!\n")
create_database()
main_menu()