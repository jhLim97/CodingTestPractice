t = int(input())

def update(datas, n):
    if n == 1:
        print(max(datas[0][0], datas[1][0]))
        return 

    datas[0][1] += datas[1][0]
    datas[1][1] += datas[0][0]

    for i in range(2, n):
        datas[0][i] += max(datas[1][i - 1], datas[1][i - 2])
        datas[1][i] += max(datas[0][i - 1], datas[0][i - 2])

    datas = sum(datas, [])
    print(max(datas))

for _ in range(t):
    n = int(input())
    datas = [list(map(int, input().split())) for _ in range(2)]
    update(datas, n)
