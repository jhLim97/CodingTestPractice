n = int(input())

result = 0
start = 0
for i in range(1, n + 1):
    start = n // i
    if start >= i:
        result += start - (i - 1)

print(result)
