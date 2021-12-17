import itertools

l, c = map(int, input().split())

alphas = list(map(str, input().split()))
alphas.sort()

moeum_list = ['a', 'e', 'i', 'o', 'u']
combination_list = list(itertools.combinations(alphas, l))

for datas in combination_list:
    count = 0
    for moeum in moeum_list:
        if moeum in datas:
            count += 1

    if count != 0 and l - count >= 2:
        print(''.join(list(datas)))
