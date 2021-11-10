l = int(input())
n = int(input())

cakes = [0] * (l + 1)
datas = []
for i in range(n):
    datas.append(list(map(int, input().split())))

max_expected_people = 0
max_real_people = 0

max_value = 0
for index, data in enumerate(datas):
    start = data[0]
    end = data[-1]
    if max_value < end - start:
        max_value = end - start
        max_expected_people = index + 1
    for d_ in range(start, end + 1):
        if cakes[d_] == 0:
            cakes[d_] = index + 1

result = list(map(lambda x: cakes.count(x), list(range(1, n + 1))))
max_real_people = result.index(max(result)) + 1

print(max_expected_people)
print(max_real_people)
