def lcm(a, b):
    for i in range(b, a * b + 1):
        if i % a == 0 and i % b == 0:
            return i

def solution(arr):
    answer = 0
    arr.sort()
    prior = arr[0]
    for i in range(1, len(arr)):
        current = arr[i]
        prior = lcm(prior, current)
    answer = prior
    return answer
