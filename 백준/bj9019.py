from collections import deque

t = int(input())

datas = [False] * 10000
type_list = ['D', 'S', 'L', 'R']

def fillDigit(value):
    if len(value) != 4:
        return '0' * (4 - len(value)) + value
    return value

def proceed(origin, target):
    datas = [False] * 10000

    queue = deque()
    queue.append((origin, ''))
    datas[origin] = True

    while queue:
        current_value, acc = queue.popleft()
        if current_value == target:
            print(acc)
            return

        nx_d = (current_value * 2) % 10000
        nx_s = (current_value - 1) % 10000

        convert_value = fillDigit(str(current_value))

        nx_l = int(convert_value[1:] + convert_value[0])
        nx_r = int(convert_value[-1] + convert_value[0:-1])

        for index, update_data in enumerate([nx_d, nx_s, nx_l, nx_r]):
            if not datas[update_data]:
                datas[update_data] = True
                queue.append((update_data, acc + type_list[index]))

for _ in range(t):
    origin, target = map(int, input().split())
    proceed(origin, target)
