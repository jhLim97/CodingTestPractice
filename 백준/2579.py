import copy

n = int(input())
scores = [int(input()) for _ in range(n)]

d = copy.deepcopy(scores)

if n == 1:
    print(d[n - 1])
else:
    d[1] = scores[0] + scores[1]
    
    if n > 2:
        d[2] = max(scores[2] + scores[0], scores[2] + scores[1])
    for i in range(3, n):
        d[i] = max(scores[i] + d[i - 2], scores[i] + scores[i - 1] + d[i - 3])

    print(d[n - 1])
