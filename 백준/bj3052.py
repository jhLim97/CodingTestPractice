data = []
for i in range(10):
    data.append(int(input()))

results = set()

for _data in data:
    result = _data % 42
    results.add(result)

print(len(results))
