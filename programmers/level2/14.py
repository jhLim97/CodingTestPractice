import copy

def solution(priorities, location):
    answer = 0
    
    queue = []
    for index, priority in enumerate(priorities):
        queue.append((priority, index))
        
    while queue:
        priority, index = queue.pop(0)
        if not queue:
            return answer + 1
        maxPri, _ = max(queue)
        if priority < maxPri:
            queue.append((priority, index))
            continue
        answer += 1
        if index == location:
            return answer
    return answer
