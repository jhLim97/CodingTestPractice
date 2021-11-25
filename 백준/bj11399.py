n = int(input())
datas = list(map(int, input().split()))

datas.sort()

sum_ = 0
result = []
for data in datas:
    sum_ += data
    result.append(sum_)

answer = sum(result)
print(answer)
