from collections import deque

def solution(numbers, target):
    answer = 0
    
    q = deque([(0, 0)])
    
    while q:
        sum, index = q.popleft()
        if index > len(numbers):
            break
        if index == len(numbers) and sum == target:
            answer += 1
        
        q.append((sum + numbers[index - 1], index + 1))
        q.append((sum - numbers[index - 1], index + 1))
    
    return answer
