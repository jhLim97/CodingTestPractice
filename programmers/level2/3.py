from collections import deque
brackets = {
    ']': '[',
    ')': '(',
    '}': '{',
}
def isAlright(s):
    stack = []
    prev = ''
    for s_ in s:
        if stack:
            prev = stack[-1]
        else:
            stack.append(s_)
            continue
        if s_ in brackets and brackets[s_] == prev:
            stack.pop()
        else:
            stack.append(s_)
    if stack:
        return False
    else:
        return True

def rotate(s, count):
    queue = deque()
    for s_ in s:
        queue.append(s_)
    for i in range(count):
        temp = queue.popleft()
        queue.append(temp)
    return ''.join(list(queue))
    
def solution(s):
    answer = 0
    for i in range(len(s)):
        rotatedS = rotate(s, i)
        if isAlright(rotatedS):
            answer += 1
    return answer
