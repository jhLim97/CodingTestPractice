count = int(input())
total = [[0] * 100 for _ in range(100)]

datas = []
for i in range(count):
    datas.append(list(map(int, input().split())))

for x, y in datas:
    for i in range(10):
        for j in range(10):
            total[x + i][y + j] = 1

total = sum(total, [])
print(total.count(1))
