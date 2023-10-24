import numpy as np

arr = np.array([1,2,3,4,5,6,7])

filter_arr = arr % 2 == 0  # Tạo mảng lọc

newarr = arr[filter_arr]  # Áp dụng mảng lọc để tạo mảng mới

print(filter_arr)
print(newarr)

#Tạo một mảng filter chỉ chứa các phần tử chẵn từ mảng gốc.