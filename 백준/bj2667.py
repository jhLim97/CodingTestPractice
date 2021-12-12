from collections import deque

n = int(input())

data = []

for _ in range(n):
    data.append(input())

result = []
count = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def update(i, j):
    global count
    queue = deque()
    queue.append((i, j))
    data[i] = data[i][:j] + '0' + data[i][j + 1:]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if data[nx][ny] == '1':
                count += 1
                data[nx] = data[nx][:ny] + '0' + data[nx][ny + 1:]
                queue.append((nx, ny))

for i in range(n):
    for j in range(n):
        if data[i][j] == '1':
            count = 1
            update(i, j)
            result.append(count)

result.sort()
print(len(result))

for result_ in result:
    print(result_)
