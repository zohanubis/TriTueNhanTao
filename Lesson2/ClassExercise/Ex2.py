import heapq

class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def astar(start, goal, h):
    open_list = []
    closed_set = set()
    start_node = Node(state=start, heuristic=h(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == goal:
            path = []
            while current_node:
                path.append((current_node.state, current_node.action))
                current_node = current_node.parent
            path.reverse()
            return path

        closed_set.add(current_node.state)

        for action, next_state, step_cost in get_successors(current_node.state):
            if next_state in closed_set:
                continue

            new_cost = current_node.cost + step_cost
            new_node = Node(
                state=next_state,
                parent=current_node,
                action=action,
                cost=new_cost,
                heuristic=h(next_state, goal),
            )

            for node in open_list:
                if node.state == next_state and node.cost <= new_cost:
                    break
            else:
                heapq.heappush(open_list, new_node)

    return None

def get_successors(state):
    # Định nghĩa các bước di chuyển và chi phí của chúng
    successors = []
    # Ví dụ: Di chuyển lên, xuống, sang trái, sang phải
    for action in ["Up", "Down", "Left", "Right"]:
        # Tính toán next_state và step_cost dựa trên action
        # Ví dụ: next_state, step_cost = move(state, action)
        successors.append((action, next_state, step_cost))
    return successors

def h(state, goal):
    # Hàm heuristic để ước tính chi phí còn lại đến goal từ state
    # Ví dụ: Manhattan distance
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

# Định nghĩa trạng thái ban đầu và trạng thái đích
start_state = (0, 0)
goal_state = (5, 5)

path = astar(start_state, goal_state, h)

if path:
    print("Đường đi từ {} đến {}:".format(start_state, goal_state))
    for state, action in path:
        print("Trạng thái: {}, Hành động: {}".format(state, action))
else:
    print("Không tìm thấy đường đi từ {} đến {}.".format(start_state, goal_state))
