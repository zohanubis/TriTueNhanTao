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