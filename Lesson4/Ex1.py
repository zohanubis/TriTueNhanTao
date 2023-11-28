def read_adjacency_matrix(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            adjacency_matrix = [list(map(int, line.strip().split())) for line in lines]
            return adjacency_matrix
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
#Ma trận 10x10
def color_graph(adjacency_matrix):
    node = "ABCDEFGHIJ"  # Cập nhật tên các đỉnh của đồ thị
    t_ = {}
    for i in range(len(adjacency_matrix)):
        t_[node[i]] = i

    degree = []  # Bậc của các đỉnh
    for i in range(len(adjacency_matrix)):
        degree.append(sum(adjacency_matrix[i]))

    colorDict = {}  # Màu có thể sử dụng để tô cho các đỉnh
    for i in range(len(adjacency_matrix)):
        colorDict[node[i]] = ["Blue", "Red", "Yellow", "Green"]

    sortedNode = []  # Sắp xếp các đỉnh theo thứ tự bậc
    indeks = []

    for i in range(len(degree)):  # Sử dụng selection sort
        _max = 0
        j = 0
        for j in range(len(degree)):
            if j not in indeks:
                if degree[j] > _max:
                    _max = degree[j]
                    idx = j
        indeks.append(idx)
        sortedNode.append(node[idx])

    theSolution = {}  # Phần xử lý tô màu (sử dụng màu ít nhất có thể)
    for n in sortedNode:
        setTheColor = colorDict[n]
        if setTheColor:  # Kiểm tra xem setTheColor có phần tử không trước khi truy cập
            theSolution[n] = setTheColor[0]
            adjacentNode = adjacency_matrix[t_[n]]
            for j in range(len(adjacentNode)):
                if adjacentNode[j] == 1 and (setTheColor[0] in colorDict[node[j]]):
                    colorDict[node[j]].remove(setTheColor[0])

    # In kết quả từng đỉnh và màu đã tô tương ứng
    for t, w in sorted(theSolution.items()):
        print("Đỉnh ", t, " = ", w)

# Sử dụng hàm để đọc ma trận từ file
file_path = r'D:\VIsual Studio Code - Github\TriTueNhanTao\Lesson4\graph10x10.txt' 
adjacency_matrix = read_adjacency_matrix(file_path)

if adjacency_matrix:
    color_graph(adjacency_matrix)

