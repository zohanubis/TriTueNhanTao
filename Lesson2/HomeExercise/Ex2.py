import heapq
import itertools

class Node:
    def __init__(self, state, path, cost, heuristic):
        self.state = state  # Trạng thái hiện tại là một danh sách các thành phố
        self.path = path  # Đường đi đã đi qua
        self.cost = cost  # Chi phí tích luỹ từ thành phố đầu tiên đến hiện tại
        self.heuristic = heuristic  # Giá trị heuristic (ở đây, là chi phí con lại)

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def tsp_a_star(cities):
    num_cities = len(cities)
    start_city = cities[0]
    goal_city = cities[0]

    # Tạo các hoán vị của thành phố trừ thành phố xuất phát
    city_permutations = list(itertools.permutations(cities[1:]))

    open_list = []
    start_node = Node([start_city], [start_city], 0, heuristic(cities, start_city, goal_city))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if len(current_node.path) == num_cities:
            # Nếu đã ghé qua tất cả thành phố, quay lại thành phố xuất phát
            current_node.path.append(start_city)
            current_node.cost += distance(current_node.state[-1], start_city)
            return current_node.path, current_node.cost

        for city in cities:
            if city not in current_node.state:
                new_path = current_node.path + [city]
                new_cost = current_node.cost + distance(current_node.state[-1], city)
                new_state = current_node.state + [city]
                new_heuristic = heuristic(cities, city, goal_city)
                new_node = Node(new_state, new_path, new_cost, new_heuristic)
                heapq.heappush(open_list, new_node)

    return None

def distance(city1, city2):
    return 0  

def heuristic(cities, current_city, goal_city):
    remaining_cities = [city for city in cities if city not in current_city]
    if not remaining_cities:
        return distance(current_city, goal_city)
    return min([distance(current_city, city) for city in remaining_cities])

def input_destination_city(cities):
    while True:
        destination = input("Nhập thành phố đích (A, B, C, D): ")
        if destination in cities:
            return destination
        else:
            print("Thành phố không hợp lệ. Vui lòng nhập lại.")

# Định nghĩa danh sách các thành phố
cities = ["A", "B", "C", "D"]

destination_city = input_destination_city(cities)

path, cost = tsp_a_star(cities)

if path:
    print("Đường đi ngắn nhất từ A đến", destination_city, "là:", path)
    print("Chi phí:", cost)
else:
    print("Không tìm thấy đường đi ngắn nhất.")
