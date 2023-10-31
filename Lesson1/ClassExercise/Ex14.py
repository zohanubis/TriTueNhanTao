import random

def randomArray(m, n):
    a = []
    for i in range(m):
        row = [random.randint(1, 100) for _ in range(n)]
        a.append(row)
    return a

def xuatDongK(a, k):
    if k < 0 or k >= len(a):
        print("Dòng không hợp lệ")
        return
    print("Dòng", k, ":", a[k])

def xuatCotK(a, k):
    if k < 0 or k >= len(a[0]):
        print("Cột không hợp lệ")
        return
    print("Cột", k, ":")
    for i in range(len(a)):
        print(a[i][k])

def timDongTongLonNhat(a):
    max_tong = 0
    dong_max = -1
    for i in range(len(a)):
        tong = sum(a[i])
        if tong > max_tong:
            max_tong = tong
            dong_max = i
    return dong_max

def timCotTichNhoNhat(a):
    min_tich = float('inf')
    cot_min = -1
    for j in range(len(a[0])):
        tich = 1
        for i in range(len(a)):
            tich *= a[i][j]
        if tich < min_tich:
            min_tich = tich
            cot_min = j
    return cot_min

def xuatDongChanCotLe(a):
    for i in range(len(a)):
        if i % 2 == 0:
            print("Dòng", i, ":")
            for j in range(len(a[0])):
                if j % 2 == 1:
                    print(a[i][j])

def tbcPhanTuChanDongLe(a):
    tong = 0
    dem = 0
    for i in range(len(a)):
        if i % 2 == 1:
            for j in range(len(a[0])):
                if a[i][j] % 2 == 0:
                    tong += a[i][j]
                    dem += 1
    if dem > 0:
        return tong / dem
    else:
        return 0

def tbcPhanTuBien(a):
    total = 0
    count = 0
    m, n = len(a), len(a[0])
    
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                total += a[i][j]
                count += 1
                
    if count > 0:
        return total / count
    else:
        return 0

def tbcTichPhanTuKhongBien(a):
    total_tich = 0
    count_tich = 0
    m, n = len(a), len(a[0])

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            tich = 1
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    tich *= a[x][y]
            total_tich += tich
            count_tich += 1

    if count_tich > 0:
        return total_tich / count_tich
    else:
        return 0



while True:
    print("-----------------------------------------------------------")
    print("Menu:")
    print("a. Tạo mảng a chứa các số nguyên ngẫu nhiên.")
    print("b. Xuất các phần tử thuộc dòng k.")
    print("c. Xuất các phần tử thuộc cột k.")
    print("d. Tìm dòng có tổng lớn nhất.")
    print("e. Tìm cột có tích nhỏ nhất.")
    print("f. Xuất ra các phần tử thuộc dòng chẵn và cột lẻ trong a.")
    print("g. Tính trung bình cộng các phần tử chẵn thuộc dòng lẻ của a.")
    print("h. Tính trung bình cộng các phần tử thuộc biên.")
    print("i. Tính trung bình tích các phần tử không thuộc biên.")
    print("j. Thoát")
    print("-----------------------------------------------------------")
    luaChon = input("Chọn bài tập (a/b/c/d/e/f/g/h/i/j): ")
    print("-----------------------------------------------------------")

    if luaChon == "a":
        m = int(input("Nhập số dòng: "))
        n = int(input("Nhập số cột: "))
        a = randomArray(m, n)
        print("Mảng a đã được tạo:")
        for row in a:
            print(row)

    elif luaChon == "b":
        k = int(input("Nhập dòng k: "))
        xuatDongK(a, k)

    elif luaChon == "c":
        k = int(input("Nhập cột k: "))
        xuatCotK(a, k)

    elif luaChon == "d":
        dong_max = timDongTongLonNhat(a)
        if dong_max != -1:
            print(f"Dòng có tổng lớn nhất > 45: Dòng {dong_max}")
        else:
            print("Không tìm thấy dòng phù hợp.")

    elif luaChon == "e":
        cot_min = timCotTichNhoNhat(a)
        if cot_min != -1:
            print(f"Cột có tích nhỏ nhất: Cột {cot_min}")
        else:
            print("Không tìm thấy cột phù hợp.")

    elif luaChon == "f":
        xuatDongChanCotLe(a)

    elif luaChon == "g":
        tbc = tbcPhanTuChanDongLe(a)
        print(f"Trung bình cộng các phần tử chẵn thuộc dòng lẻ: {tbc}")

    elif luaChon == "h":
        tbc = tbcPhanTuBien(a)
        print(f"Trung bình cộng các phần tử thuộc biên: {tbc}")

    elif luaChon == "i":
        tbc_tich = tbcTichPhanTuKhongBien(a)
        print(f"Trung bình tích các phần tử không thuộc biên: {tbc_tich}")

    elif luaChon == "0":
        print("Kết thúc chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
