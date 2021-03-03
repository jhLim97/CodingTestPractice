n,m = map(int, input().split())
datas = list(map(int, input().split()))

datas.sort()

start = 0
end = max(datas)

result = 0
while(start <= end):
  mid = (start + end)//2
  sum = 0
  
  for data in datas:
    if data > mid:
      sum += data - mid

  if m <= sum:
    result = mid
    start = mid + 1
  else:
    end = mid - 1
  
print(result)
