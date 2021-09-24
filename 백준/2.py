n, m, l = map(int, input().split())
seats = [0] * n
count = 0

if m == 0:
    print(1)

def convert(index):
    if index < 0:
        index += len(seats)
    elif index >= len(seats):
        index -= len(seats)
    return index

index = 0
while True:
    index = convert(index)
    seats[index] += 1
    value = seats[index]
    if value == m:
        break
    if value % 2 == 0:
        index -= l
    else:
        index += l
    count += 1
print(count)
