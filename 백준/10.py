mushrooms = []
for i in range(10):
    mushrooms.append(int(input()))

result = 0
for index, mushroom in enumerate(mushrooms):
    result += mushroom
    if result == 100:
        break
    if result > 100:
        under100_diffrence = 100 - (result - mushroom)
        over100_diffrence = result - 100

        result = result if over100_diffrence <= under100_diffrence else result - mushroom
        break

print(result)
