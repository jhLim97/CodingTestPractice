t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())

    flag = False
    while x <= n * m:
        if x % n == y % n:
            print(x)
            flag = True
            break
        x += m

    if not flag:
        print(-1)
