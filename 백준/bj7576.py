from collections import deque

m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))

result = 0
for graph_row in graph:
    for row in graph_row:
        if row == 0:
            print(-1)
            exit(0)
    result = max(result, max(graph_row))
print(result - 1)
