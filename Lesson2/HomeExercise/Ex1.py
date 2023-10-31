import copy
from heapq import heappush, heappop

m = 4

rows = [1, 0, -1, 0]
cols = [0, 1, 0, -1]

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, key):
        heappush(self.heap, key)

    def pop(self):
        return heappop(self.heap)

    def empty(self):
        return not self.heap

class Node:
    def __init__(self, parent, state, empty_tile_pos, cost, level):
        self.parent = parent
        self.state = state
        self.empty_tile_pos = empty_tile_pos
        self.cost = cost
        self.level = level

    def __lt__(self, other):
        return self.cost < other.cost

def calculateMisplacedTiles(state, goal):
    count = 0
    for i in range(n):
        for j in range(n):
            if state[i][j] and state[i][j] != goal[i][j]:
                count += 1
    return count

def createNewNode(state, empty_tile_pos, new_empty_tile_pos, level, parent, goal):
    new_state = copy.deepcopy(state)
    x1, y1 = empty_tile_pos
    x2, y2 = new_empty_tile_pos
    new_state[x1][y1], new_state[x2][y2] = new_state[x2][y2], new_state[x1][y1]
    cost = calculateMisplacedTiles(new_state, goal)
    return Node(parent, new_state, new_empty_tile_pos, cost, level)

def printMatrix(state):
    for i in range(n):
        for j in range(n):
            print("%2d " % state[i][j], end=" ")
        print()

def isValid(x, y):
    return 0 <= x < n and 0 <= y < n

def printPath(root):
    if root is None:
        return
    printPath(root.parent)
    printMatrix(root.state)
    print()

def solvePuzzle(initial, empty_tile_pos, goal):
    pq = PriorityQueue()

    initial_cost = calculateMisplacedTiles(initial, goal)
    root = Node(None, initial, empty_tile_pos, initial_cost, 0)

    pq.push(root)

    while not pq.empty():
        minimum = pq.pop()

        if minimum.cost == 0:
            printPath(minimum)
            return

        for i in range(m):
            x, y = minimum.empty_tile_pos
            new_x = x + rows[i]
            new_y = y + cols[i]
            if isValid(new_x, new_y):
                child = createNewNode(minimum.state, minimum.empty_tile_pos, (new_x, new_y), minimum.level + 1, minimum, goal)
                pq.push(child)

# Nhập giá trị n từ bàn phím
n = int(input("Nhập giá trị n (kích thước của bảng n-Puzzle): "))

# Tạo trạng thái ban đầu và trạng thái mục tiêu dựa trên giá trị n
initial_state = [[0] * n for _ in range(n)]
goal_state = [[0] * n for _ in range(n)]

for i in range(n):
    initial_state[i] = list(map(int, input(f"Nhập hàng {i + 1} của trạng thái ban đầu: ").split()))

for i in range(n):
    goal_state[i] = list(map(int, input(f"Nhập hàng {i + 1} của trạng thái mục tiêu: ").split()))

empty_tile_position = None
for i in range(n):
    for j in range(n):
        if initial_state[i][j] == 0:
            empty_tile_position = (i, j)
            break

solvePuzzle(initial_state, empty_tile_position, goal_state)
