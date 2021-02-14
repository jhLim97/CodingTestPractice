n = int(input())

data = []

for i in range(n):
  data.append(int(input()))

data.sort()
data.reverse()

for i in range(n):
  print(data[i], end=' ')
