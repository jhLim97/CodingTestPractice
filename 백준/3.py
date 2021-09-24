n = int(input())
priorMaxNum = 1
count = 1
while True:
    if n == 1:
        count = 0
        break
    if n <= priorMaxNum + 6 * count:
        break
    priorMaxNum += 6 * count
    count += 1

print(count + 1)
