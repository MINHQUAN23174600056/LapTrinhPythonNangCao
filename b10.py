import math
class Point:
    def __init__(self, x=0, y=0):
        self.x = x 
        self.y = y 
    def display(self):
        print(f"Tọa độ điểm: ({self.x}, {self.y})")

# Lớp Ellipse kế thừa từ Point
class Ellipse(Point):
    def __init__(self, x=0, y=0, major_axis=1, minor_axis=1):
        #Gọi hàm tạo của lớp cha Point
        super().__init__(x, y)
        self.major_axis = major_axis  # Bán trục lớn
        self.minor_axis = minor_axis  # Bán trục nhỏ
    
    #Phương thức nhập bán trục lớn và bán trục nhỏ
    def input_axes(self):
        self.major_axis = float(input("Nhập bán trục lớn: "))
        self.minor_axis = float(input("Nhập bán trục nhỏ: "))
    
    #Phương thức tính diện tích elip
    def area(self):
        return math.pi * self.major_axis * self.minor_axis
    def display(self):
        super().display()  # Hiển thị tọa độ điểm gốc
        print(f"Bán trục lớn: {self.major_axis}")
        print(f"Bán trục nhỏ: {self.minor_axis}")
        print(f"Diện tích elip: {self.area()}")

# Lớp Đường tròn kế thừa từ Ellipse
class Circle(Ellipse):
    def __init__(self, x=0, y=0, radius=1):
        #Đường tròn là elip có bán trục lớn = bán trục nhỏ = bán kính
        super().__init__(x, y, radius, radius)
    def input_radius(self):
        radius = float(input("Nhập bán kính đường tròn: "))
        self.major_axis = self.minor_axis = radius

    #Phương thức tính diện tích đường tròn
    def area(self):
        return math.pi * (self.major_axis ** 2)  # Diện tích đường tròn = π * r^2
    
    #Phương thức hiển thị thông tin về đường tròn
    def display(self):
        super().display()  # Hiển thị tọa độ điểm gốc
        print(f"Bán kính đường tròn: {self.major_axis}")
        print(f"Diện tích đường tròn: {self.area()}")
ellipse = Ellipse()
ellipse.input_axes()
ellipse.display()
circle = Circle()
circle.input_radius()
circle.display()