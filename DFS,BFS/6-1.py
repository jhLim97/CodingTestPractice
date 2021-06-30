import itertools

n = int(input())
datas = list(map(int, input().split()))
numbers = list(map(int, input().split()))

operaters = []
d = {
  0 : '+',
  1 : '-',
  2 : '*',
  3 : '//'
}

for i, number in enumerate(numbers):
  for j in range(number):
    operaters.append(d[i])

combi = list(itertools.permutations(operaters, n - 1))

max_ = -int(1e9)
min_ = int(1e9)

for combi_ in set(combi):
  for i, data in enumerate(datas):
    if i == 0:
      val = data
      continue
    operater = combi_[i - 1]
    if operater == '+':
      val += data
    elif operater == '-':
      val -= data
    elif operater == '*':
      val *= data
    else:
      if val < 0:
        val = - (val * (-1) // data)
      else:
        val = val // data
  max_ = max(max_, val)
  min_ = min(min_, val)

print(max_)
print(min_)
