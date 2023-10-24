class Sach:
    dic_sach = {"masach": [], "tensach": [], "dongia": [], "soluong": []}

    def __init__(self, n):
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

    def inThongTinCuonSach(self, index):
        ma = self.dic_sach['masach'][index]
        ten = self.dic_sach['tensach'][index]
        dg = self.dic_sach['dongia'][index]
        sl = self.dic_sach['soluong'][index]
        print(f"Ma sach: {ma}, Ten sach: {ten}, Don gia: {dg}, So luong: {sl}")

sach_obj = Sach(3)

for i in range(3):
    sach_obj.inThongTinCuonSach(i)

# Tính tổng số lượng sách
tong_so_luong_sach = sum(sach_obj.dic_sach['soluong'])
print("Tong so luong sach: " + str(tong_so_luong_sach))

# Xuất tên các sách có số lượng > 10
print("Sach co so luong lon hon 10:")

for i in range(len(sach_obj.dic_sach["masach"])):
    if sach_obj.dic_sach["soluong"][i] > 10:
        print(sach_obj.dic_sach["tensach"][i])
