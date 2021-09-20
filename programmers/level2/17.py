def solution(brown, yellow):
    answer = []
    width = brown + yellow
    for x in range(1, width // 2):
        if width % x != 0:
            continue
        y = width // x
        if brown == 2 * (x + y - 2):
            return [y, x]
    return answer
