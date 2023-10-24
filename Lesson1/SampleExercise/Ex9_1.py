class Sach:
    dic_sach = {"masach": [], "tensach": [], "dongia": [], "soluong": []}

    def __init__(self, n):
        self.nhapThongTin(n)
        self.inThongTin()
        self.tongSoLuong()
        self.sachSLHon10()

    def nhapThongTin(self, n):
        for i in range(n):
            ma = input("Nhap ma sach: ")
            ten = input("Nhap ten sach: ")
            dg = float(input("Nhap don gia: "))
            sl = int(input("Nhap so luong: "))

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
        print(f"Ma sach: {ma}, Ten sach: {ten}, Don gia: {dg}, So luong: {sl}")

    def tongSoLuong(self):
        tong_so_luong_sach = sum(self.dic_sach['soluong'])
        print("Tong so luong sach: " + str(tong_so_luong_sach))

    def sachSLHon10(self):
        print("Sach co so luong lon hon 10:")
        for i in range(len(self.dic_sach["masach"])):
            if self.dic_sach["soluong"][i] > 10:
                print(self.dic_sach["tensach"][i])

# Tạo một đối tượng sách với 3 cuốn sách và thực hiện các chức năng
sach_obj = Sach(3)
