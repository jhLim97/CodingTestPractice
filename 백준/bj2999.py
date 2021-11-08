message = input()
n = len(message)
r = c = 0
for i in range(1, int(n**(1/2)) + 1):
    if n % i == 0:
        r, c = i, n // i

data = [[''] * c for _ in range(r)]
cnt = 0
for i in range(c):
    for j in range(r):
        data[j][i] = message[cnt]
        cnt += 1

data = sum(data, [])
data = ''.join(data)
print(data)
