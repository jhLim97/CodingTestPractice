answer = 0
def dfs(numbers, target, level, result):
    global answer
    if level == len(numbers):
        if result == target:
            answer += 1
        return
    dfs(numbers, target, level + 1, result + numbers[level])
    dfs(numbers, target, level + 1, result - numbers[level])

def solution(numbers, target):
    global answer
    dfs(numbers, target, 0, 0)
    
    return answer
