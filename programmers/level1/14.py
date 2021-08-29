def solution(arr):
    answer = []
    current = -1
    for _, number in enumerate(arr):
        if current == number:
            continue
        current = number
        answer.append(number)
    return answer
