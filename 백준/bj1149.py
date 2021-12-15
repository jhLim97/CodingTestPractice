n = int(input())

datas = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    datas[i][0] = (datas[i][0] + min(datas[i - 1][1], datas[i - 1][2]))
    datas[i][1] = (datas[i][1] + min(datas[i - 1][0], datas[i - 1][2]))
    datas[i][2] = (datas[i][2] + min(datas[i - 1][0], datas[i - 1][1]))

print(min(datas[n - 1]))
