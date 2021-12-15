from collections import defaultdict, deque
import sys

n = int(input())
m = int(input())

graph_dic = defaultdict(list)
for _ in range(m):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph_dic[start].append((end, weight))

start, end = map(int, input().split())

queue = deque()

datas = [10000000000] * (n + 1)
datas[start] = 0

queue.append((datas[start], start))

while queue:
    dist, start = queue.popleft()

    if datas[start] < dist:
        continue

    for targets in graph_dic[start]:
        target, weight = targets
        if datas[target] > weight + dist:
            datas[target] = weight + dist
            queue.append((datas[target], target))

print(datas[end])
