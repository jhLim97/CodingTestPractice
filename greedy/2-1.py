n, m = map(int, input().split())

result = 0
for i in range(n):
  data = list(map(int, input().split()))
  data.sort()

  if result < data[0]:
    result = data[0]

print(result)