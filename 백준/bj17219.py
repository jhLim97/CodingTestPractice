from collections import defaultdict

n, m = map(int, input().split())

dic = defaultdict()
for i in range(n):
    address, password = map(str, input().split())
    dic[address] = password

for i in range(m):
    print(dic[input()])
