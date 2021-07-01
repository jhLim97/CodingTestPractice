from collections import deque

def compare(word, temp):
    count = 0
    
    for i in range(len(word)):
        if word[i] != temp[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    q = deque([(begin, 0)])
    while q:
        temp, level = q.popleft()
        if temp == target:
            return level
        for word in words:
            if compare(word, temp):
                q.append((word, level + 1))
    return answer
