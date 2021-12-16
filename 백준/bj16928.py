from collections import deque, defaultdict

n, m = map(int, input().split())

ladders = defaultdict(int)
snakes = defaultdict(int)

for i in range(n):
    start, end = map(int, input().split())
    ladders[start] = end

for i in range(m):
    start, end = map(int, input().split())
    snakes[start] = end

visited = [False] * 101

queue = deque()
queue.append((1, 0))
visited[1] = True

while queue:
    x, count = queue.popleft()

    if x == 100:
        print(count)
        break

    for i in range(1, 7):
        nx = x + i

        if nx in ladders:
            nx = ladders[nx]
        if nx in snakes:
            nx = snakes[nx]

        if nx <= 100 and not visited[nx]:
            queue.append((nx, count + 1))
            visited[nx] = True
