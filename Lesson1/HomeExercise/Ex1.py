def tronMang(a, b):
    i, j = 0, 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])

    return result

# Mảng a và b ban đầu
a = [3, 9, 1, 4]
b = [2, 7, 4, 3, 2, 8]

ket_qua = tronMang(a, b)
print("Mảng kết quả:", ket_qua)
