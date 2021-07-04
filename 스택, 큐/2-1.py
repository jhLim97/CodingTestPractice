from collections import deque, defaultdict

def solution(progresses, speeds):
    answer = []
    
    q = deque()
    for progress, speed in zip(progresses, speeds):
        q.append((progress, speed))
        
    time = 1
    table = defaultdict(int)
    while q:
        progress, speed = q.popleft()
        while (progress + (time * speed)) < 100:
               time += 1
        table[time] += 1
               
    for value in table.values():
        answer.append(value)
    
    return answer
