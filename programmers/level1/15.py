def solution(n):
    answer = []
    base = 10
    for i in range(len(str(n))):
        answer.append(n % base)
        n = n // base
    return answer
