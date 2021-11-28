n, k = map(int, (input().split()))

women = [0] * 7
men = [0] * 7

for _ in range(n):
    s, y = map(int, input().split())

    if s == 0:
        women[y] += 1
        continue
    men[y] += 1

answer = 0

for w_ in women[1:]:
    mod = w_ // k
    rest = w_ % k
    rest = 1 if rest != 0 else 0
    answer += (mod + rest)

for w_ in men[1:]:
    mod = w_ // k
    rest = w_ % k
    rest = 1 if rest != 0 else 0
    answer += (mod + rest)

print(answer)
