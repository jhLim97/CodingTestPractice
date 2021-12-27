from collections import deque
import copy

n, m = map(int, input().split())
datas = [list(map(int, input().split())) for _ in range(n)]

max_safety_area = 0

def proceed():
    global max_safety_area
    copy_datas = copy.deepcopy(datas)

    visited = [[False] * m for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    queue = deque()
    for i in range(n):
        for j in range(m):
            if copy_datas[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if copy_datas[nx][ny] != 0 or visited[nx][ny]:
                continue

            copy_datas[nx][ny] = 2
            visited[nx][ny] = True
            queue.append((nx, ny))

    safety_area = sum(data.count(0) for data in copy_datas)
    max_safety_area = max(max_safety_area, safety_area)

def wall(count):
    if count == 3:
        proceed()
        return

    for i in range(n):
        for j in range(m):
            if datas[i][j] == 0:
                datas[i][j] = 1
                wall(count + 1)
                datas[i][j] = 0

wall(0)
print(max_safety_area)
