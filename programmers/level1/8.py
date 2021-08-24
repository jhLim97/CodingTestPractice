from collections import defaultdict
def helper(total):
    if total >= 90:
        return 'A'
    elif total >= 80:
        return 'B'
    elif total >= 70:
        return 'C'
    elif total >= 50:
        return 'D'
    else:
        return 'F'
def solution(scores):
    answer = ''
    studentNumber = len(scores)
    result = defaultdict(list)
    for i, score in enumerate(scores):
        for j, score_  in enumerate(score):
            result[j + 1].append(score_)
    for i in range(1, studentNumber + 1):
        myGrade = result[i][i - 1]
        maxValue = max(result[i])
        minValue = min(result[i])
        maxCount = result[i].count(maxValue)
        minCount = result[i].count(minValue)
        if maxCount == 1 and myGrade == maxValue:
            result[i] = list(filter(lambda x: x != maxValue, result[i]))
        if minCount == 1 and myGrade == minValue:
            result[i] = list(filter(lambda x: x != minValue, result[i]))
        answer += helper(sum(result[i]) / len(result[i])) if len(result[i]) != 0 else 'F'
    return answer
