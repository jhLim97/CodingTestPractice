def solution(price, money, count):
    total = 0
    for i in range(1, count + 1):
        total += i
    neededPrice = total * price
    answer = neededPrice - money if neededPrice > money else 0
    return answer
