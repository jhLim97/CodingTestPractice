n = int(input())

datas = {}
turn = 'A'


def get_data(i):
    global datas, turn
    this_turn = list(map(int, input().split()))
    data = sorted(this_turn[1:], reverse=True)

    datas[str(i) + turn] = data

    if turn == 'A':
        turn = 'B'
    else:
        turn = 'A'


for i in range(1, n + 1):
    get_data(i)
    get_data(i)


def compare(a, b):
    count = min(len(a), len(b))
    for a_, b_ in zip(a, b):
        if a_ > b_:
            return 'A'
        elif a_ < b_:
            return  'B'

    if len(a) == len(b):
        return 'D'

    return 'A' if len(a) > len(b) else 'B'

result = []
temp_list = []
for key, value in datas.items():
    if key.find('A') == -1:
        result.append(compare(temp_list, value))
    else:
        temp_list = value

for result_ in result:
    print(result_)
