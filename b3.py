import math
class Phan_so:
    def __init__(self, tu_so=0, mau_so=1):
        self.tu_so = tu_so
        self.mau_so = mau_so
        if self.mau_so == 0:
            raise ValueError("Mẫu số không thể bằng 0.")
    def dieu_kien(self):
        return self.mau_so != 0
    def nhap_phan_so(self):
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))
        if not self.dieu_kien():
            raise ValueError("Mẫu số không thể bằng 0")
    def rut_gon(self):
        ucln = math.gcd(self.tu_so, self.mau_so)
        self.tu_so //= ucln
        self.mau_so //= ucln
    def in_phan_so(self):
        self.rut_gon()
        if self.mau_so == 1:
            print(f"Phân số: {self.tu_so}")
        else:
            print(f"Phân số: {self.tu_so}/{self.mau_so}")
ps = Phan_so()
ps.nhap_phan_so()
ps.in_phan_so()