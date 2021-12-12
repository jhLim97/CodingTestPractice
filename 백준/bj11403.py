n = int(input())

graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for graph_ in graph:
    print(' '.join(map(str, graph_)))
