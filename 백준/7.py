count = int(input())
total = [[0] * 101 for _ in range(101)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

datas = []
for i in range(count):
    datas.append(list(map(int, input().split())))

for x, y in datas:
    for i in range(10):
        for j in range(10):
            total[x + i][y + j] = 1

result = 0
for i in range(1, 101):
    for j in range(1, 101):
        if total[i][j] == 1:
            cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if total[nx][ny] == 1:
                    cnt += 1
            if cnt == 2:
                result += 2
            if cnt == 3:
                result += 1

print(result)
