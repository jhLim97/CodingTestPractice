from collections import deque
def helper(a, b):
    count = 0
    for a_, b_ in zip(a, b):
        if a_ != b_:
            count += 1
    return count == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    queue = deque([(begin, 0)])
    while queue:
        temp, value = queue.popleft()
        for word in words:
            if temp == target:
                return value
            if helper(temp, word):
                queue.append((word, value + 1))
    return 0
