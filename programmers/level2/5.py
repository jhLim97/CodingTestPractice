def solution(s):
    data = s.split(" ")
    numbers = []
    for i in data:
        numbers.append(int(i))
    numbers.sort()
    return str(numbers[0]) + " " + str(numbers[len(numbers) - 1])
