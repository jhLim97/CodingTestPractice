
n, k = map(int, input().split())
cnt = 0

while True:
  target = (n//k)*k
  cnt += (n-target)
  n = target

  if n<k:
    break

  cnt += 1
  n //= k

cnt += (n-1)
print(cnt)
