from collections import deque

n, k = map(int, input().split())

position = [abs(k - n)] * 100001
position[n] = 0

queue = deque()
queue.append(n)

while queue:
    x = queue.popleft()
    if x == k:
        break
    if x - 1 >= 0 and position[x - 1] > position[x]:
        position[x - 1] = position[x] + 1
        queue.append(x - 1)
    if x + 1 <= 100000 and position[x + 1] > position[x]:
        position[x + 1] = position[x] + 1
        queue.append(x + 1)
    if x * 2 <= 100000 and position[x * 2] > position[x]:
        position[x * 2] = position[x] + 1
        queue.append(x * 2)

print(position[k])

