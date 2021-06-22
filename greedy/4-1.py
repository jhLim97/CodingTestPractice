def helper(visited, start, name):
    front_visited = visited[:start] + [True] * (len(name) - start)
    back_visited = [True] * (start + 1) + visited[start + 1:] 

    min_distance = 21
    index = start
    for i, f in enumerate(front_visited):
        if not f:
            if min_distance > start - i:
                min_distance = start - i
                index = i

    for i, b in enumerate(back_visited):
        if not b:
            if min_distance > i - start:
                min_distance = i - start
                index = i
            if min_distance > start + len(name) - i:
                min_distance = start + len(name) - i
                index = i 
    return min_distance, index

def solution(name):
    answer = 0

    visited = [False] * len(name)
    for i, alpha in enumerate(name):
        if alpha == 'A':
            visited[i] = True

    start = 0
    min_distance = 0
    while False in visited:
        visited[start] = True
        answer += min(ord(name[start]) - ord('A'), ord('Z') - ord(name[start]) + 1)
        answer += min_distance
        min_distance, start  = helper(visited, start, name)
        if min_distance == 21:
            break
    return answer
