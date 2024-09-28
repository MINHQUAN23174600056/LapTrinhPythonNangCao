class thi_sinh:
    def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa
    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa
    def in_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}, Điểm Toán: {self.diem_toan}, Điểm Lý: {self.diem_ly}, Điểm Hóa: {self.diem_hoa}, Tổng điểm: {self.tinh_tong_diem()}")

def nhap_danh_sach_ts():
    danh_sach = []
    so_ts = int(input("Nhập số lượng thí sinh: "))
    for i in range(so_ts):
        ho_ten = input(f"Nhập họ tên thí sinh thứ {i+1}: ")
        diem_toan = float(input("Nhập điểm Toán: "))
        diem_ly = float(input("Nhập điểm Lý: "))
        diem_hoa = float(input("Nhập điểm Hóa: "))
        ts = thi_sinh(ho_ten, diem_toan, diem_ly, diem_hoa)
        danh_sach.append(ts)
    return danh_sach

def in_ds_trung_tuyen(danh_sach, diem_chuan=20):
    #Lọc danh sách thí sinh có tổng điểm >= điểm chuẩn
    danh_sach_trung_tuyen = [ts for ts in danh_sach if ts.tinh_tong_diem() >= diem_chuan]
    #Sắp xếp danh sách theo tổng điểm từ cao xuống thấp
    danh_sach_trung_tuyen.sort(key=lambda ts: ts.tinh_tong_diem(), reverse=True)
    print(f"\nDanh sách thí sinh trúng tuyển (điểm chuẩn >= {diem_chuan}):")
    for ts in danh_sach_trung_tuyen:
        ts.in_thong_tin()
danh_sach_ts = nhap_danh_sach_ts()
in_ds_trung_tuyen(danh_sach_ts)