# Khai báo ma trận kề
G = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
]

# Tên các đỉnh
nodes = ["L", "M", "P", "Be", "R", "V", "Ber", "Lx", "Bru", "H"]

# Màu cấm tô
for i in range(len(nodes)):
    print(f"Đỉnh {nodes[i]} có màu cấm tô: {i + 1}")

# Bậc của các đỉnh
degree = [sum(G[i]) for i in range(len(G))]

# In thông tin bậc của các đỉnh
print("\nBậc của các đỉnh:")
for i in range(len(nodes)):
    print(f"{nodes[i]}: {degree[i]}")

# Hạ bậc từng cấp
for k in range(1, 7):
    print(f"\nHạ bậc lần {k}:")
    for i in range(len(nodes)):
        if degree[i] > 0:
            print(f"{nodes[i]}: ", end="")
            for j in range(len(nodes)):
                if G[i][j] == 1:
                    degree[j] -= 1
                    print(f"{nodes[j]}*, ", end="")
            print()

# Kết quả màu tô
colors = [1, 2, 1, 3, 2, 1, 2, 4, 3, 1]
print("\nMàu tô của các đỉnh:")
for i in range(len(nodes)):
    print(f"{nodes[i]}: {colors[i]}")
