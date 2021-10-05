datas = []
result = []
for i in range(4):
    datas.append(list(map(int, input().split())))

def helper(data):
    x1, y1 = data[0], data[1]
    x2, y2 = data[2], data[3]
    x3, y3 = data[4], data[5]
    x4, y4 = data[6], data[7]

    if x2 < x3 or x1 > x4 or y2 < y3 or y1 > y4:
        return 'd'
    elif (x2 == x3 and y1 == y4) or (x2 == x3 and y2 == y3) or (x4 == x1 and y2 == y3) or (x4 == x1 and y4 == y1):
        return 'c'
    elif (x2 == x3 and (y4 > y1 and y3 < y2)) or (x4 == x1 and (y4 > y1 and y3 < y2)) or (y1 == y4 and (x4 > x1 and x3 < x2)) or (y2 == y3 and (x3 < x2 and x4 > x1)):
        return 'b'
    else:
        return 'a'

for i in range(4):
    result.append(helper(datas[i]))

for i in range(4):
    print(result[i])
