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
