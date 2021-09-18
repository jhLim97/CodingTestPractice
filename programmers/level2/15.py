from collections import deque

def solution(prices):
    answer = []
    queue = deque()
    for price in prices:
        queue.append(price)
    
    while queue:
        price = queue.popleft()
        time = 0
        for price_ in queue:
            if price <= price_:
                time += 1
            else:
                time += 1
                break
        answer.append(time)
    
    return answer
