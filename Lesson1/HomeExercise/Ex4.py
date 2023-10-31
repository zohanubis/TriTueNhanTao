def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            print("Nội dung của file:")
            print(content)
    except FileNotFoundError:
        print("File không tồn tại!")

def write_file(file_name):
    content = input("Nhập nội dung muốn ghi vào file: ")
    with open(file_name, "w") as file:
        file.write(content)
        print("Nội dung đã được ghi vào file.")

def append_to_file(file_name):
    content = input("Nhập nội dung muốn thêm vào file: ")
    with open(file_name, "a") as file:
        file.write("\n" + content)
        print("Nội dung mới đã được thêm vào file.")

def main():
    while True:
        print("\nChọn một trong các chức năng sau:")
        print("1. Đọc nội dung từ file")
        print("2. Ghi nội dung vào file")
        print("3. Thêm nội dung vào file đã tồn tại")
        print("4. Thoát chương trình")

        choice = input("Nhập lựa chọn của bạn: ")

        if choice == "1":
            file_name = input("Nhập tên file bạn muốn đọc: ")
            read_file(file_name)
        elif choice == "2":
            file_name = input("Nhập tên file bạn muốn ghi: ")
            write_file(file_name)
        elif choice == "3":
            file_name = input("Nhập tên file bạn muốn thêm nội dung: ")
            append_to_file(file_name)
        elif choice == "4":
            print("Thoát chương trình")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
