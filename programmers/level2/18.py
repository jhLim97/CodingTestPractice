from collections import defaultdict
def solution(clothes):
    answer = 1
    dic = defaultdict(int)
    for cloth in clothes:
        dic[cloth[1]] += 1
    for dic_ in dic.values():
        answer *= (dic_ + 1)
    return answer - 1 
