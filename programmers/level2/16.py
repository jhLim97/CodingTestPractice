def solution(citations):
    length = len(citations)
    citations.sort()
    answer = 0
    for i in range(1, length + 1):
        for j in range(length):
            if i <= citations[j] and i <= len(citations[j:length]):
                answer = i
    return answer
