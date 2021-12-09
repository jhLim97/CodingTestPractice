n = int(input())

data = [n + 1] * (n + 1)
data[n] = 0

while n != 1:
    if n % 3 == 0:
        one = n // 3
        count = data[n] + 1
        data[one] = count if count <= data[one] else data[one]
    if n % 2 == 0:
        two = n // 2
        count = data[n] + 1
        data[two] = count if count <= data[two] else data[two]

    three = n - 1
    count = data[n] + 1
    data[three] = count if count <= data[three] else data[three]

    n -= 1

print(data[1])
