def input_matrix(m, n):
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            value = int(input(f"Nhập giá trị tại hàng {i + 1}, cột {j + 1}: "))
            row.append(value)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()

def sum_upper_diagonal(matrix):
    total = 0
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            total += matrix[i][j]
    return total

def absolute_values(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = abs(matrix[i][j])

def replace_even(matrix, x):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 2 == 0:
                matrix[i][j] = x

def all_even(matrix):
    for row in matrix:
        for element in row:
            if element % 2 != 0:
                return False
    return True

def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def is_main_diagonal_increasing(matrix):
    n = len(matrix)
    for i in range(n - 1):
        if matrix[i][i] >= matrix[i + 1][i + 1]:
            return False
    return True

def lower_diagonal(matrix):
    n = len(matrix)
    lower = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(matrix[i][j])
        lower.append(row)
    return lower

def is_sub_diagonal_decreasing(matrix):
    lower = lower_diagonal(matrix)
    n = len(lower)
    for i in range(n - 1):
        if lower[i][i] <= lower[i + 1][i + 1]:
            return False
    return True

def main():
    m = int(input("Nhập số dòng của ma trận: "))
    n = int(input("Nhập số cột của ma trận: "))
    matrix = input_matrix(m, n)
    print("Ma trận ban đầu:")
    print_matrix(matrix)
    while True:
        print("\nChọn một trong các chức năng sau:")
        print("a. Tính tổng các phần tử thuộc tam giác trên của đường chéo phụ kể cả đường chéo phụ trong ma trận vuông a cấp n.")
        print("b. Chuyển các phần tử âm thành trị tuyệt đối của nó trong a.")
        print("c. Thay các phần tử chẵn trong a bằng số nguyên x cho trước.")
        print("d. Kiểm tra a có toàn chẵn không?")
        print("e. Kiểm tra a có đối xứng không.")
        print("f. Kiểm tra ma trận vuông a cấp n có đường chéo chính tăng dần không.")
        print("g. Xuất các phần tử thuộc tam giác dưới của đường chéo phụ kể cả đường chéo phụ trong ma trận vuông a cấp n.")
        print("h. Kiểm tra ma trận vuông a cấp n có đường chéo phụ giảm dần không.")
        print("i. Thoát chương trình.")
        
        choice = input("Nhập lựa chọn của bạn: ")

        if choice == 'a':
            total = sum_upper_diagonal(matrix)
            print(f"Tổng các phần tử thuộc tam giác trên của đường chéo phụ kể cả đường chéo phụ: {total}")
        elif choice == 'b':
            absolute_values(matrix)
            print("Ma trận sau khi chuyển các phần tử âm thành trị tuyệt đối:")
            print_matrix(matrix)
        elif choice == 'c':
            x = int(input("Nhập giá trị x: "))
            replace_even(matrix, x)
            print(f"Ma trận sau khi thay các phần tử chẵn bằng {x}:")
            print_matrix(matrix)
        elif choice == 'd':
            if all_even(matrix):
                print("Ma trận a toàn chẵn.")
            else:
                print("Ma trận a không toàn chẵn.")
        elif choice == 'e':
            if is_symmetric(matrix):
                print("Ma trận a đối xứng.")
            else:
                print("Ma trận a không đối xứng.")
        elif choice == 'f':
            if is_main_diagonal_increasing(matrix):
                print("Ma trận a có đường chéo chính tăng dần.")
            else:
                print("Ma trận a không có đường chéo chính tăng dần.")
        elif choice == 'g':
            lower = lower_diagonal(matrix)
            print("Các phần tử thuộc tam giác dưới của đường chéo phụ kể cả đường chéo phụ:")
            print_matrix(lower)
        elif choice == 'h':
            if is_sub_diagonal_decreasing(matrix):
                print("Ma trận a có đường chéo phụ giảm dần.")
            else:
                print("Ma trận a không có đường chéo phụ giảm dần.")
        elif choice == 'i':
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
