import heapq

def solution(scoville, K):
    answer = 0
    
    heap = []
    for scovill in scoville:
        heapq.heappush(heap, scovill)
    
    while heap[0] < K:
        if len(heap) <= 1:
            return -1
        a, b = heapq.heappop(heap), heapq.heappop(heap) 
        heapq.heappush(heap, a + b * 2)
        answer += 1
    
    return answer
