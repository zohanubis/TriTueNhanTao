def read_adjacency_matrix(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            adjacency_matrix = [list(map(int, line.strip().split())) for line in lines]
            return adjacency_matrix
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def color_schedule(adjacency_matrix):
    teams = "ABCDEF"  # Tên các đội
    t_ = {}

    if len(teams) != len(adjacency_matrix):
        print("Số lượng đội không khớp với kích thước ma trận.")
        return
    
    for i in range(len(teams)):
        t_[teams[i]] = i

    # Màu có thể sử dụng để tô cho các trận đấu
    colorDict = {}
    for i in range(len(adjacency_matrix)):
        colorDict[teams[i]] = ["Black"]

    # Tô màu các trận đấu đã diễn ra
    for i in range(len(adjacency_matrix)):
        for j in range(i + 1, len(adjacency_matrix)):
            if adjacency_matrix[i][j] == 1:
                colorDict[teams[i]].append(teams[j])
                colorDict[teams[j]].append(teams[i])

    # Sắp xếp các đội theo số trận đấu đã diễn ra (ít trận đấu đến nhiều trận đấu)
    sortedTeams = sorted(teams, key=lambda x: len(colorDict[x]))

    # Phần xử lý tô màu tối ưu
    schedule = {}
    for team in sortedTeams:
        available_colors = ["Black", "Red", "Green", "Blue", "Yellow"]  # Thêm màu tùy chọn nếu cần
        for neighbor in colorDict[team]:
            if neighbor in schedule and schedule[neighbor] in available_colors:
                available_colors.remove(schedule[neighbor])
        schedule[team] = available_colors[0]

    # In kết quả lịch thi đấu tối ưu
    for team, color in schedule.items():
        print("Đội ", team, " sẽ thi đấu màu ", color)

# Sử dụng hàm để đọc ma trận từ file
file_path = 'D:\VIsual Studio Code - Github\TriTueNhanTao\Lesson4\Ex3_matrix.txt'
adjacency_matrix = read_adjacency_matrix(file_path)

if adjacency_matrix:
    color_schedule(adjacency_matrix)

