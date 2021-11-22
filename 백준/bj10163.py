n = int(input())

datas = []
for i in range(n):
    data = list(map(int, input().split()))
    datas.append(data)

values = [[-1] * 1001 for _ in range(1001)]

for index, data in enumerate(datas):
    x, y, width, height = data[0], data[1], data[2], data[3]

    for i in range(x, x + width):
        values[i][y:y + height] = [index] * height

for i in range(len(datas)):
    result = 0
    for cnt in range(1001):
        result += values[cnt].count(i)
    print(result)
