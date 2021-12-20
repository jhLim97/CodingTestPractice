data = input()

splited_by_minus = data.split('-')
result = 0

for i, data in enumerate(splited_by_minus):
    data = data.split('+')
    data = list(map(lambda x : int(x), data))

    result += sum(data) if i == 0 else -sum(data)

print(result)
