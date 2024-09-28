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
        print(f"Ngày {self.day}/{self.month}/{self.year}")
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
date = Date(28, 2, 2024)
date.display()
print("Ngày tiếp theo:")
date.next()
date.display()