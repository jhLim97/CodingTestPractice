n,k = map(int, input().split())

data_1 = list(map(int, input().split()))
data_2 = list(map(int, input().split()))

data_1.sort()
data_2 = sorted(data_2, reverse=True)

for i in range(k):
  if data_1[i] < data_2[i]:
    data_1[i], data_2[i] = data_2[i], data_1[i]; 
  else: break;

print(sum(data_1))
