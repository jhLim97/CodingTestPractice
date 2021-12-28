from collections import deque, defaultdict
import sys, heapq

v, e = map(int, input().split())
start_v = int(input())

INF = int(1e9)
result = [INF] * (v + 1)
result[start_v] = 0

edges_dic = defaultdict(list)
for _ in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    edges_dic[u].append((v, w))

# queue = deque()
# queue.append(start_v)
queue = []
heapq.heappush(queue, (0, start_v))

while queue:
    # depart = queue.popleft()
    dist, depart = heapq.heappop(queue)

    if result[depart] < dist:
        continue

    for arrive, w in edges_dic[depart]:
        cost = dist + w
        if result[arrive] > cost:
            result[arrive] = cost
            #queue.append(arrive)
            heapq.heappush(queue, (cost, arrive))

for result_ in result[1:]:
    if result_ == INF:
        print('INF')
        continue
    print(result_)
