while True:
    print("---------------------------------------------------------------------")    
    print("Menu:")
    print("1. Tính tổng, hiệu, tích, thương của hai số (Ex 1)")
    print("2. Lấy các ký tự từ chỉ số 2 đến chỉ số 4 của chuỗi (Ex 2)")
    print("3. Xử lý chuỗi (Ex 3)")
    print("4. So sánh a và b (Ex 4)")
    print("5. In 'Yes' hoặc 'No' nếu a bằng b (Ex 5)")
    print("6. In 1 nếu a bằng b, in 2 nếu a > b, in 3 nếu ngược lại (Ex 6)")
    print("7. In ra 'Hello World!' nếu a bằng b và b bằng d (Ex 7)")
    print("8. In ra 'Hello World!' nếu a bằng b hoặc c bằng d (Ex 8)")
    print("9. So sánh a và b (Ex 9)")
    print("10. So sánh a và b, in A nếu a > b, = nếu a = b, B nếu a < b (Ex 10)")
    print("11. Thoát")
    print("---------------------------------------------------------------------")

    luaChon = input("Chọn bài tập (1/2/3/4/5/6/7/8/9/10/11): ")

    if luaChon == "1":
        a = float(input("Nhập giá trị a: "))
        b = float(input("Nhập giá trị b: "))
        tong = a + b
        hieu = a - b
        tich = a * b
        if b != 0:
            thuong = a / b
        else:
            thuong = "Không thể chia cho 0"
        print(f"Tổng của {a} và {b} là: {tong}")
        print(f"Hiệu của {a} và {b} là: {hieu}")
        print(f"Tích của {a} và {b} là: {tich}")
        print(f"Thương của {a} và {b} là: {thuong}")

    elif luaChon == "2":
        chuoi = "Hello World"
        chuoi_cat = chuoi[2:5]
        print(f"Kết quả sau khi cắt: {chuoi_cat}")

    elif luaChon == "3":
        chuoi = " Hello World "
        chuoi = chuoi.strip()
        chuoi_hoa = chuoi.upper()
        chuoi_thuong = chuoi.lower()
        chuoi_thay_the = chuoi.replace('H', 'J')

        print("Chuỗi sau khi xử lí:")
        print("Chuỗi sau khi xóa khoảng trắng thừa:", chuoi)
        print("Chuỗi sau khi chuyển sang dạng hoa:", chuoi_hoa)
        print("Chuỗi sau khi chuyển sang dạng thường:", chuoi_thuong)
        print("Chuỗi sau khi thay thế 'H' thành 'J':", chuoi_thay_the)

    elif luaChon == "4":
        a = input("Nhập giá trị a: ")
        b = input("Nhập giá trị b: ")
        if a > b:
            print("Hello World!")
        else:
            print("Error: a < b")

    elif luaChon == "5":
        a = input("Input a: ")
        b = input("Input b: ")
        if a == b:
            print("Yes")
        else:
            print("No")

    elif luaChon == "6":
        a = input("Input a: ")
        b = input("Input b: ")
        if a == b:
            print("KQ: 1")
        elif a > b:
            print("KQ: 2")
        else:
            print("KQ: 3")

    elif luaChon == "7":
        a = input("Input a: ")
        b = input("Input b: ")
        if a == "b" and b == "d":
            print("Hello World!")

    elif luaChon == "8":
        a = input("Input a: ")
        b = input("Input b: ")
        c = input("Input c: ")
        if a == "b" or c == "d":
            print("Hello World!")

    elif luaChon == "9":
        a = input("Input a: ")
        b = input("Input b: ")
        print("Yes" if a > b else "No")

    elif luaChon == "10":
        a = float(input("Nhập a: "))
        b = float(input("Nhập b: "))
        print("A" if a > b else "=" if a == b else "B")

    elif luaChon == "11":
        print("Kết thúc chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
