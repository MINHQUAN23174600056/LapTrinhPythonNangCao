#Lớp Date đã xây dựng ở bài trước
class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year
    def is_leap_year(self):
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            return True
        return False
    def days_in_month(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month in [4, 6, 9, 11]:
            return 30
        elif self.month == 2:
            if self.is_leap_year():
                return 29
            else:
                return 28
    def display(self):
        return f"{self.day}/{self.month}/{self.year}"
    def next(self):
        days_in_current_month = self.days_in_month()
        if self.day < days_in_current_month:
            self.day += 1
        else:
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1
class Employee:
    def __init__(self, name, birth_date, hire_date):
        self.name = name  
        self.birth_date = birth_date  
        self.hire_date = hire_date  
    @staticmethod
    def input_employee():
        name = input("Nhập họ tên nhân viên: ")
        print("Nhập ngày sinh: ")
        birth_day = int(input("Ngày: "))
        birth_month = int(input("Tháng: "))
        birth_year = int(input("Năm: "))
        birth_date = Date(birth_day, birth_month, birth_year)
        print("Nhập ngày vào công ty: ")
        hire_day = int(input("Ngày: "))
        hire_month = int(input("Tháng: "))
        hire_year = int(input("Năm: "))
        hire_date = Date(hire_day, hire_month, hire_year)
        return Employee(name, birth_date, hire_date)
    def display(self):
        print(f"Họ tên nhân viên: {self.name}")
        print(f"Ngày sinh: {self.birth_date.display()}")
        print(f"Ngày vào công ty: {self.hire_date.display()}")
employee = Employee.input_employee()
print("Thông tin nhân viên:")
employee.display()