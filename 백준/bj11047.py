n, k = map(int, input().split())

data = []
for _ in range(n):
    a = int(input())
    data.append(a)

count = 0
for data_ in data[::-1]:
    count += k // data_
    k = k % data_
    if k == 0:
        break

print(count)
