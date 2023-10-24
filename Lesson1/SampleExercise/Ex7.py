import numpy as np

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42  # Tạo mảng lọc

newarr = arr[filter_arr]  # Áp dụng mảng lọc để tạo mảng mới

print(filter_arr)
print(newarr)
