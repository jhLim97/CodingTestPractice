from collections import deque

n, k = map(int, input().split())

graph = []

for i in range(n):
  graph.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

data = []
for i in range(n):
  for j in range(n):
    if graph[i][j] != 0:
      data.append((graph[i][j], i, j))

second = 0
data.sort()
q = deque(data)
while second < s:
  length = len(q)
  for i_ in range(length):
    level, x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if graph[nx][ny] == 0:
        graph[nx][ny] = level
        q.append((level, nx, ny))
  second += 1
    
print(graph)
print(graph[x - 1][y - 1])
    
