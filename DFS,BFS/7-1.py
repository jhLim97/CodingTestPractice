import sys
sys.setrecursionlimit(10**6)

n, l, r = map(int, input().split())

graph = [[] for i in range(n)]

for i in range(n):
  data = list(map(int, input().split()))
  graph[i].extend(data)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = [[False] * n for i in range(n)]
def dfs(x, y, data):
  visited[x][y] = True
  count = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
      continue
    val = abs(graph[x][y] - graph[nx][ny])  
    if val >= l and val <= r:
      data.append((nx, ny))
      dfs(nx, ny, data)  
      count += 1
  if count == 0:
    return False
  else:
    return True

def change(data):
  sum = 0
  for x, y in data:
    sum += graph[x][y]
  
  for x, y in data:
    graph[x][y] = sum // len(data)

answer = 0
while True:
  go = 0
  for i in range(n):
    for j in range(n):
      data = [(i, j)]
      if not visited[i][j] and dfs(i, j, data):
        change(data)
        go += 1
  visited = [[False] * n for i in range(n)]
  if go == 0:
    break
  answer += 1
print(answer)
