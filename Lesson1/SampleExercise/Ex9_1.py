class Sach:
    dic_sach = {"masach": [], "tensach": [], "dongia": [], "soluong": []}

    def __init__(self, n):
        self.nhapThongTin(n)
        self.inThongTin()
        self.tongSoLuong()
        self.sachSLHon10()

    def nhapThongTin(self, n):
        for i in range(n):
            ma = input("\nNhập mã sách: ")
            ten = input("Nhập tên sách: ")
            dg = float(input("Nhập đơn giá: "))
            sl = int(input("Nhập số lượng: "))

            # Thêm thông tin của sách vào từ điển
            self.dic_sach['masach'].append(ma)
            self.dic_sach['tensach'].append(ten)
            self.dic_sach['dongia'].append(dg)
            self.dic_sach['soluong'].append(sl)

    def inThongTin(self):
        for i in range(len(self.dic_sach["masach"])):
            self.inThongTin_cuon_sach(i)

    def inThongTin_cuon_sach(self, index):
        ma = self.dic_sach['masach'][index]
        ten = self.dic_sach['tensach'][index]
        dg = self.dic_sach['dongia'][index]
        sl = self.dic_sach['soluong'][index]
        print(f"Mã sách: {ma}, Tên sách: {ten}, Đơn giá: {dg}, Số lượng: {sl}")
# Tính tổng số lượng sách

    def tongSoLuong(self):
        tong_so_luong_sach = sum(self.dic_sach['soluong'])
        print("Tổng số lượng sách: " + str(tong_so_luong_sach))

# Xuất tên các sách có số lượng > 10

    def sachSLHon10(self):
        print("Sách có số lượng lớn hơn 10:")
        for i in range(len(self.dic_sach["masach"])):
            if self.dic_sach["soluong"][i] > 10:
                print(self.dic_sach["tensach"][i])

sach_obj = Sach(3)
