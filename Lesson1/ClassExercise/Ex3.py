chuoi = " Hello World "

# Xóa khoảng trắng thừa ở đầu và cuối chuỗi
chuoi = chuoi.strip()

# Chuyển chuỗi sang dạng hoa và thường
chuoi_hoa = chuoi.upper()
chuoi_thuong = chuoi.lower()

# Thay ký tự 'H' thành ký tự 'J'
chuoi_thay_the = chuoi.replace('H', 'J')

print("Chuỗi sau khi xử lí:")
print("Chuỗi sau khi xóa khoảng trắng thừa:", chuoi)
print("Chuỗi sau khi chuyển sang dạng hoa:", chuoi_hoa)
print("Chuỗi sau khi chuyển sang dạng thường:", chuoi_thuong)
print("Chuỗi sau khi thay thế 'H' thành 'J':", chuoi_thay_the)
