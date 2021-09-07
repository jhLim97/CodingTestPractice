def solution(n):
    if n <= 2:
        return 1
    two_prior = 1
    prev = 1
    for i in range(3, n + 1):
        prev, two_prior = two_prior + prev, prev
    return prev % 1234567
