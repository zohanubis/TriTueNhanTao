a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

print("A" if a > b else "=" if a == b else "B")
# Nếu a lớn hơn b, sẽ in ra "A". 
# Nếu a và b bằng nhau, sẽ in ra "=". 
# Nếu a nhỏ hơn b, sẽ in ra "B"