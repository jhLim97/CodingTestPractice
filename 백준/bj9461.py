t = int(input())

datas = [0] * 101
datas[1] = 1
datas[2] = 1
datas[3] = 1
datas[4] = 2
datas[5] = 2

for _ in range(t):
    n = int(input())
    for i in range(6, n + 1):
        datas[i] = datas[i - 1] + datas[i - 5]

    print(datas[n])
