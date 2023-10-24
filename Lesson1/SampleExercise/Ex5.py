#Viết hàm trộn 2 mảng một chiều thành 1 mảng một chiều với mỗi phần tử của mảng
#mới là tổng của 2 phần tương ứng từ 2 mảng cho trước. Trong quá trình trộn 2 mảng
#nếu mảng nào còn phần tử thì các phần tử còn lại của mảng đó sẽ đưa vào mảng mới


a = [3,9,1,4]
b = [2,7,4,3,8,2]
min = len(b) if len (a) > len(b) else len(a)
c = a if len(a) > len(b) else b
for i in range (min) :
    c[i] = a[i] + b[i]
print(c)