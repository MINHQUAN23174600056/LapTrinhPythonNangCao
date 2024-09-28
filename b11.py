import math
# Lớp Tam Giác
class Tam_giac:
    def __init__(self, a=1, b=1, c=1):
        self.a = a  
        self.b = b  
        self.c = c  
    
    #Phương thức kiểm tra xem ba cạnh có tạo thành một tam giác hay không
    def is_valid(self):
        return self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.b
    
    #Phương thức tính chu vi
    def perimeter(self):
        return self.a + self.b + self.c
    
    #Phương thức tính diện tích tam giác bằng công thức Hê-rông
    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    
    #Phương thức hiển thị thông tin tam giác
    def display(self):
        print(f"Cạnh a: {self.a}, Cạnh b: {self.b}, Cạnh c: {self.c}")
        if self.is_valid():
            print(f"Chu vi tam giác: {self.perimeter()}")
            print(f"Diện tích tam giác: {self.area()}")
        else:
            print("Ba cạnh không tạo thành một tam giác hợp lệ")

# Lớp Tam Giác Vuông kế thừa từ Tam_giac
class Tam_giac_vuong(Tam_giac):
    def __init__(self, a=1, b=1, c=1):
        super().__init__(a, b, c)
    
    #Phương thức kiểm tra xem tam giác có phải là tam giác vuông không
    def is_right_triangle(self):
        sides = sorted([self.a, self.b, self.c])  
        return math.isclose(sides[2]**2, sides[0]**2 + sides[1]**2)
    
    #Phương thức hiển thị thông tin tam giác vuông
    def display(self):
        super().display()
        if self.is_valid():
            if self.is_right_triangle():
                print("Đây là tam giác vuông")
            else:
                print("Đây không phải là tam giác vuông")

# Lớp Tam Giác Cân kế thừa từ Tam_giac
class Tam_giac_can(Tam_giac):
    def __init__(self, a=1, b=1):
        super().__init__(a, b, b)  #2 cạnh bằng nhau
    
    #Phương thức kiểm tra tam giác cân
    def is_isosceles(self):
        return self.a == self.b or self.b == self.c or self.c == self.a
    
    #Phương thức hiển thị thông tin tam giác cân
    def display(self):
        super().display()
        if self.is_valid():
            print("Đây là tam giác cân")

# Lớp Tam Giác Đều kế thừa từ Tam_giac_can
class EquilateralTriangle(Tam_giac_can):
    def __init__(self, a=1):
        super().__init__(a, a)  #3 cạnh đều bằng nhau
    #Phương thức kiểm tra tam giác đều
    def is_equilateral(self):
        return self.a == self.b == self.c
    #Phương thức hiển thị thông tin tam giác đều
    def display(self):
        super().display()
        if self.is_valid() and self.is_equilateral():
            print("Đây là tam giác đều")

if __name__ == "__main__":
    print("Chọn loại tam giác:")
    print("1. Tam giác thường")
    print("2. Tam giác vuông")
    print("3. Tam giác cân")
    print("4. Tam giác đều")
    choice = int(input("Nhập lựa chọn: "))
    if choice == 1:
        a = float(input("Nhập cạnh a: "))
        b = float(input("Nhập cạnh b: "))
        c = float(input("Nhập cạnh c: "))
        triangle = Tam_giac(a, b, c)
        triangle.display()
    elif choice == 2:
        a = float(input("Nhập cạnh a: "))
        b = float(input("Nhập cạnh b: "))
        c = float(input("Nhập cạnh c: "))
        right_triangle = Tam_giac_vuong(a, b, c)
        right_triangle.display()
    elif choice == 3:
        a = float(input("Nhập cạnh a (cạnh bên): "))
        b = float(input("Nhập cạnh đáy: "))
        isosceles_triangle = Tam_giac_can(a, b)
        isosceles_triangle.display()
    elif choice == 4:
        a = float(input("Nhập cạnh tam giác đều: "))
        equilateral_triangle = EquilateralTriangle(a)
        equilateral_triangle.display()
    else:
        print("Lựa chọn không hợp lệ")
