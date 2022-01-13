def solution(N, stages):
    stages.sort()
    
    result = []
    totalCount = len(stages)
    for i in range(1, N + 1):
        if totalCount == 0:
            result.append((0, i))
        else:
            proceed = stages.count(i)
            result.append((proceed/totalCount, i))
            totalCount -= proceed
        
    result.sort(key = lambda x : (-x[0], x[1]))
    result = list(map(lambda x : x[1], result))
    
    return result
