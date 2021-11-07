n = int(input())
seats = input()

seats = seats.replace('LL', 'l')

answer = 1 + len(seats)
if answer > n:
    answer = n
print(answer)
