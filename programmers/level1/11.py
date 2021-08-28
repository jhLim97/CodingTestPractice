import itertools
def solution(numbers):
    answer = set()
    result = list(itertools.combinations(numbers, 2))
    for _, item in enumerate(result):
        answer.add(sum(item))
    answer = sorted(list(answer))
    return answer
