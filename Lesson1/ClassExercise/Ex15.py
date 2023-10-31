class SINHVIEN:
    def __init__(self, ma_sv, ten, nam_sinh, diem_tb):
        self.ma_sv = ma_sv
        self.ten = ten
        self.nam_sinh = nam_sinh
        self.diem_tb = diem_tb

def kiemTraDuKieuKien(sv):
    return sv.diem_tb >= 5

def sinhVien20Tuoi(sv):
    nam_hien_tai = 2023
    return nam_hien_tai - sv.nam_sinh == 20

def sinhVienHeDaiHoc(sv):
    return "DH" in sv.ma_sv[2:4]

def demSVTheoTen(arr, ten):
    return sum(1 for sv in arr if sv.ten == ten)

def demSVTheoHo(arr, ho):
    return sum(1 for sv in arr if sv.ten.split()[0] == ho)

def main():
    SV_Arr = [
        SINHVIEN("SV001", "Nguyễn Công Nhân", 2003, 6.5),
        SINHVIEN("SV002", "Trần Văn Bằng", 2002, 4.8),
        SINHVIEN("SV003", "Lê Thị Lan", 2000, 5.7),
        SINHVIEN("SV004", "Phan Đăng Dũng", 2001, 7.2),
    ]

    while True:
        
        print("\nMenu:")
        print("1. Kiểm tra sinh viên đủ điều kiện lên lớp.")
        print("2. Xuất sinh viên đủ 20 tuổi.")
        print("3. Đếm số sinh viên học hệ đại học.")
        print("4. Đếm số sinh viên có tên «Lan».")
        print("5. Đếm số sinh viên có họ «Phan».")
        print("0. Thoát chương trình.")
        print("---------------------------------------------------")
        choice = input("Chọn một tùy chọn (1/2/3/4/5/0): ")
        print("---------------------------------------------------")

        if choice == "1":
            duDK = sum(1 for sv in SV_Arr if kiemTraDuKieuKien(sv))
            print(f"Có {duDK} sinh viên đủ điều kiện lên lớp.")
        elif choice == "2":
            sinhVien20Tuoi_arr = [sv for sv in SV_Arr if sinhVien20Tuoi(sv)]
            print("Sinh viên đủ 20 tuổi:")
            for sv in sinhVien20Tuoi_arr:
                print(sv.ma_sv, sv.ten, sv.nam_sinh)
        elif choice == "3":
            sl = sum(1 for sv in SV_Arr if sinhVienHeDaiHoc(sv))
            print(f"Có {sl} sinh viên học hệ đại học.")
        elif choice == "4":
            sl = demSVTheoTen(SV_Arr, "Le Thi Lan")
            print(f"Có {sl} sinh viên có tên «Lan».")
        elif choice == "5":
            sl= demSVTheoHo(SV_Arr, "Phan")
            print(f"Có {sl} sinh viên có họ «Phan».")
        elif choice == "0":
            print("Chương trình kết thúc.")
            break
        else:
            print("Tùy chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
    
