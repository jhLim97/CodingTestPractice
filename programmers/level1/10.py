def helper(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    return count
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if helper(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
