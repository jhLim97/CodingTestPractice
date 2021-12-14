n = int(input())

datas = []
for _ in range(n):
    row = list(map(int, input().split()))
    datas.append(row)

for i in range(1, n):
    for j in range(len(datas[i])):
        if j == 0:
            datas[i][j] += datas[i - 1][0]
        elif j == len(datas[i]) - 1:
            datas[i][j] += datas[i - 1][j - 1]
        else:
            datas[i][j] += max(datas[i - 1][j - 1], datas[i - 1][j])

print(max(datas[n - 1]))
