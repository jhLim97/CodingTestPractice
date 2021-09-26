from collections import defaultdict

n = int(input())
dic = defaultdict(list)
maxWidth, maxHeight = 0, 0
minWidth, minHeight = 0, 0

twoPrior, twoPriorValue = -1, -1
prior, priorValue = 0, 0
for i in range(6):
    direction, value = map(int, input().split())
    if direction == twoPrior:
        if prior in [3, 4]:
            minWidth = priorValue
        else:
            minHeight = priorValue
    if prior == 0:
        firstDirection, firstValue = direction, value
    if i == 5:
        lastDirection, lastValue = direction, value

    twoPrior, twoPriorValue = prior, priorValue
    prior, priorValue = direction, value
    dic[direction].append(value)

for item in dic.keys():
    if len(dic[item]) == 1:
        maxValue = max(dic[item])
        if item in [3, 4]:
            maxWidth = maxValue
        else:
            maxHeight = maxValue

if minWidth == 0:
    if firstDirection in [3, 4]:
        minWidth = firstValue
    else:
        minWidth = lastValue
if minHeight == 0:
    if firstDirection in [1, 2]:
        minHeight = firstValue
    else:
        minHeight = lastValue

answer = maxWidth * maxHeight - minWidth * minHeight
print(answer * n)
