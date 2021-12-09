t = int(input())

result = 0
def update(sum, target):
    global result

    if sum > target:
        return
    elif sum == target:
        result += 1
        return
    else:
        for i in range(1, 4):
            update(sum + i, target)

for _ in range(t):
    target = int(input())
    result = 0
    update(0, target)
    print(result)
