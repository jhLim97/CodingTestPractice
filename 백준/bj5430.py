from collections import deque
t = int(input())

def proceed():
    global operations, converted_datas
    count = 0

    queue = deque(converted_datas)
    for operation in operations:
        if operation == 'R':
            count += 1
        else:
            if len(queue) == 0:
                print('error')
                return

            if count % 2 != 0:
                queue.pop()
            else:
                queue.popleft()

    result = list(queue)
    if count % 2 != 0:
        result.reverse()
    print('[' + ','.join(map(str, result)) + ']')

for i in range(t):
    operations = list(map(str, input()))
    count = int(input())
    input_datas = input()
    input_datas = input_datas.replace('[', '')
    input_datas = input_datas.replace(']', '')
    converted_datas = list(map(int, input_datas.split(','))) if len(input_datas) > 0 else []

    proceed()
