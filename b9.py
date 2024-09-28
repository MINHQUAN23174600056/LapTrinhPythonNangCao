# Lớp Đa giác
class Da_giac:
    def __init__(self, num_sides):
        self.num_sides = num_sides  
        self.sides = [0] * num_sides 
    def input_sides(self):
        for i in range(self.num_sides):
            self.sides = float(input(f"Nhập độ dài cạnh thứ {i+1}: "))
    def display_sides(self):
        for i in range(self.num_sides):
            print(f"Cạnh {i+1}: {self.sides[i]}")
    
# Lớp Hình bình hành kế thừa từ Da_giac
class Hinh_binh_hanh(Da_giac):
    def __init__(self):
        super().__init__(4)
        self.height = 0  
    def input_dimensions(self):
        self.input_sides()
        self.height = float(input("Nhập chiều cao: "))
    # Phương thức tính chu vi hình bình hành
    def perimeter(self):
        return 2 * (self.sides[0] + self.sides[1])
    # Phương thức tính diện tích hình bình hành
    def area(self):
        return self.sides[0] * self.height
    

# Lớp Hình chữ nhật kế thừa từ Hinh_binh_hanh
class Hinh_chu_nhat(Hinh_binh_hanh):
    def __init__(self):
        super().__init__()
    def input_dimensions(self):
        #Hình chữ nhật có 2 cặp cạnh bằng nhau
        self.sides[0] = float(input("Nhập chiều dài: "))
        self.sides[1] = float(input("Nhập chiều rộng: "))
        self.sides[2] = self.sides[0]  
        self.sides[3] = self.sides[1]
    # Phương thức tính chu vi hình chữ nhật
    def perimeter(self):
        return 2 * (self.sides[0] + self.sides[1])
    # Phương thức tính diện tích hình chữ nhật
    def area(self):
        return self.sides[0] * self.sides[1]
    
# Lớp Hình vuông kế thừa từ Hinh_chu_nhat
class Hinh_vuong(Hinh_chu_nhat):
    def __init__(self):
        super().__init__()
    def input_dimensions(self):
        side_length = float(input("Nhập độ dài cạnh: "))
        self.sides = [side_length] * 4
    
    #Phương thức tính chu vi hình vuông
    def perimeter(self):
        return 4 * self.sides[0]
    #Phương thức tính diện tích hình vuông
    def area(self):
        return self.sides[0] ** 2
    
if __name__ == "__main__":
    print("Chọn loại hình để tính toán:")
    print("1. Hình bình hành")
    print("2. Hình chữ nhật")
    print("3. Hình vuông")
    choice = int(input("Nhập lựa chọn: ")) 
    if choice == 1:
        parallelogram = Hinh_binh_hanh()
        parallelogram.input_dimensions()
        print(f"Chu vi hình bình hành: {parallelogram.perimeter()}")
        print(f"Diện tích hình bình hành: {parallelogram.area()}")
    
    elif choice == 2:
        rectangle = Hinh_chu_nhat()
        rectangle.input_dimensions()
        print(f"Chu vi hình chữ nhật: {rectangle.perimeter()}")
        print(f"Diện tích hình chữ n:{rectangle.area()}")
    
    elif choice == 3:
        square = Hinh_vuong()
        square.input_dimensions()
        print(f"Chu vi hình vuông: {square.perimeter()}")
        print(f"Diện tích hình vuông: {square.area()}")
    else:
        print("Lựa chọn không hợp lệ")