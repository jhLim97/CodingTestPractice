#방법 1
def dfs(visited, computers, x):
    if visited[x]:
        return
    visited[x] = True
    for i, computer in enumerate(computers[x]):
        if computer == 1 and not visited[i]:
            dfs(visited, computers, i)

def solution(n, computers):
    answer = 0

    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(visited, computers, i)
            answer += 1

    return answer

#방법 2
from collections import deque

def bfs(graph, i, visited):
    q = deque([i])
    while q:
        vertex = q.popleft()
        visited[vertex] = True
        for g_ in graph[vertex]:
            if not visited[g_]:
                q.append(g_)

def solution(n, computers):
    answer = 0
    
    graph = [[] for i in range(n + 1)]
    for i, computer in enumerate(computers):
        for j in range(n):
            if computer[j] == 1 and i != j:
                graph[i + 1].append(j + 1)
    
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            bfs(graph, i, visited)
            answer += 1
    return answer
