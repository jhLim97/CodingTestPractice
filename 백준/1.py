number = int(input())
switches = [-1] + list(map(int, input().split()))

studentNumber = int(input())
studentInfo = []
for i in range(studentNumber):
    temp = tuple(map(int, input().split()))
    studentInfo.append(temp)


def isBalance(left, right):
    return switches[left] == switches[right]

def male(number):
    for i in range(number, len(switches), number):
        change(i)

def female(number):
    change(number)
    for i in range(1, len(switches)):
        left, right = number - i, number + i
        if left < 1 or right >= len(switches):
            return
        if isBalance(left, right):
            change(left)
            change(right)
        else:
            break


def change(i):
    if switches[i] == 1:
        switches[i] = 0
    else:
        switches[i] = 1

for info in studentInfo:
    gender, number = info
    if gender == 1:
        male(number)
    else:
        female(number)

for i, value in enumerate(switches):
    if i == 0:
        continue
    print(value, end=' ')
    if i % 20 == 0:
        print()
