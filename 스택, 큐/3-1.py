from collections import deque
import copy

def solution(priorities, location):
    answer = 0
    
    q = deque()
    for index, priority in enumerate(priorities):
        q.append((index, priority))
    
    while q:
        success = True
        index, priority = q.popleft()
        for i, p in copy.deepcopy(q):
            if p > priority:
                q.append((index, priority))
                success = False
                break
        if not success:
            continue
            
        answer += 1
        if index == location:
            return answer
    
    return answer
