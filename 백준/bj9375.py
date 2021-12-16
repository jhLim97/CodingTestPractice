from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())

    if n == 0:
        print(0)
        continue

    clothes = defaultdict(list)
    for i in range(n):
        name, clothe_type = map(str, input().split())
        clothes[clothe_type].append(name)

    count = 1
    for cloth_list in clothes.values():
        count *= (len(cloth_list) + 1)

    print(count - 1)
