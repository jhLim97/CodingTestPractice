def helper(n):
    nTobin = bin(n)
    countOne = nTobin.count('1')
    return countOne
def solution(n):
    nTobin = bin(n)
    countOne = nTobin.count('1')
    while True:
        n += 1
        if helper(n) == countOne:
            break
    return n
