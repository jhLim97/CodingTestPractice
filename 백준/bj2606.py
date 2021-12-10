from collections import defaultdict

n = int(input())
t = int(input())

data = defaultdict(list)
check_list = [False] * (n + 1)
for _ in range(t):
    start, end = map(int, input().split())
    data[start].append(end)
    data[end].append(start)

result = []
def update(i):
    if check_list[i]:
        return

    result.append(i)
    linked = data[i]
    check_list[i] = True
    for linked_ in linked:
        update(linked_)

update(1)
print(len(result) - 1)
