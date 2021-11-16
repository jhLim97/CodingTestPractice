n = int(input())

datas = []
result = []

for i in range(n):
    datas.append(input())

for data in datas:
    score = 0
    prev = ''
    acc = 0
    for d_ in data:
        if d_ == 'O':
            prev = 'O'
            if prev == 'O':
                acc += 1
            else:
                acc = 1
            score += acc
        else:
            prev = ''
            acc = 0
    result.append(score)

for result_ in result:
    print(result_)
