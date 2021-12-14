n = int(input())

datas = []

for _ in range(n):
    start, end = map(int, input().split())
    datas.append((start, end))

datas.sort(key = lambda x : x[0])
datas.sort(key = lambda x : x[1])

last = 0
count = 0

for start, end in datas:
    if start >= last:
        last = end
        count += 1
        
print(count)
