from collections import deque
import copy

def helper(data):
    sum = 0
    for weight, level in data:
        sum += weight
    return sum

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    q = deque()
    for w in truck_weights:
        q.append(w)
        
    total_weight = deque()
    while q:
        w = q[0]
        for i, (w_, level_) in enumerate(copy.deepcopy(total_weight)):
            total_weight[i][1] = level_ + 1
        if len(total_weight) > 0:    
            if total_weight[0][1] > bridge_length:
                total_weight.popleft()
        if len(total_weight) < bridge_length and helper(total_weight) + w <= weight:
            total_weight.append([q.popleft(), 1])
        answer += 1
    answer += (bridge_length - min(total_weight, key = lambda x : x[1])[1] + 1)
    return answer
