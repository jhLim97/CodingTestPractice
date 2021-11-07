from itertools import permutations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

possible_data = list(permutations(cards, 3))
sum_datas = list(map(lambda x: sum(x), possible_data))
datas_under_m = list(filter(lambda x: x <= m, sum_datas))

print(max(datas_under_m))
