class HinhChuNhat:
    def __init__(self,):
        self.chieu_dai = 0
        self.chieu_rong = 0
    def input(self):
        self.chieu_dai = float(input("Nhập chiều dài của hcn: "))
        self.chieu_rong = float(input("Nhập chiều rộng của hcn: "))
    def chu_vi(self):
        return 2*(self.chieu_dai + self.chieu_rong)
    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong
    def print(self,chu_vi,dien_tich):
        self.chu_vi() = chu_vi
        self.dien_tich() = dien_tich
        print("Chiều dài: ",self.chieu_dai)
        print("Chiều rộng: ",self.chieu_rong)
        print("Chu vi: ",self.chu_vi)
        print("Diện tích :",self.dien_tich)
hcn = HinhChuNhat()
hcn.input()
hcn.print()