def dfs(visited, computers, i):
    if visited[i]:
        return
    visited[i] = True
    for index, computer_ in enumerate(computers[i]):
        if computer_:
            dfs(visited, computers, index)    
def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(len(computers)):
        if not visited[i]:
            dfs(visited, computers, i)
            answer += 1

    return answer
