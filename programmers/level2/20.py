def solution(A,B):
    answer = 0

    A.sort()
    B = sorted(B, reverse = True)
    
    for a, b in zip(A, B):
        answer += a * b

    return answer
