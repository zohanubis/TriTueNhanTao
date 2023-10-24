while True:
    print("Menu:")
    print("11. Tạo mảng b chỉ chứa phần tử chẵn của mảng a")
    print("12. Tính tổng các số từ 0 đến 999 là bội của 3 hoặc 5")
    print("13. Trộn 2 mảng một chiều và tính tổng từng cặp phần tử")
    print("14. Thoát")

    luaChon = input("Chọn bài tập (11/12/13/14): ")

    if luaChon == "11":
        n = int(input("Nhập số phần tử của mảng a: "))
        a = []
        for i in range(n):
            a.append(int(input(f"Nhập phần tử thứ {i+1}: ")))

        b = [x for x in a if x % 2 == 0]
        print("Mảng a:", a)
        print("Mảng b (chứa phần tử chẵn của a):", b)

    elif luaChon == "12":
        total = 0
        for i in range(1000):
            if i % 3 == 0 or i % 5 == 0:
                total += i
        print(f"Tổng các số từ 0 đến 999 là bội của 3 hoặc 5: {total}")

    elif luaChon == "13":
        # Nhập mảng a
        m = int(input("Nhập số phần tử của mảng a: "))
        a = []
        for i in range(m):
            a.append(int(input(f"Nhập phần tử thứ {i+1} của mảng a: ")))

        # Nhập mảng b
        n = int(input("Nhập số phần tử của mảng b: "))
        b = []
        for i in range(n):
            b.append(int(input(f"Nhập phần tử thứ {i+1} của mảng b: ")))

        # Trộn mảng và tính tổng từng cặp phần tử
        result = []
        for i in range(max(m, n)):
            sum_ab = (a[i] if i < m else 0) + (b[i] if i < n else 0)
            result.append(sum_ab)

        print("Mảng a:", a)
        print("Mảng b:", b)
        print("Mảng kết quả sau khi trộn và tính tổng từng cặp phần tử:", result)

    elif luaChon == "14":
        print("Kết thúc chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
