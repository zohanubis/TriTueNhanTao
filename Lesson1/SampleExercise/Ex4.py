#Viết chương trình tính tổng các số từ 0 đến n mà là bội của 3 hoặc 5
sum = 0
n = 11
for i in range(n):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print(f"Tong cac so tu 0 den {n} ma la boi cua 3 hoac 5 la: {sum}")
        