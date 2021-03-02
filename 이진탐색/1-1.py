n = int(input())
dataN = list(map(int, input().split()))
m = int(input())
dataM = list(map(int, input().split()))

result = []

dataN.sort()

def binarySearch(data, start, end, target):
  if start > end:
    return False

  mid = (start + end) // 2

  if target == data[mid]:
    return True
  elif target > data[mid]:
    return binarySearch(data, mid + 1, end, target)
  else:
    return binarySearch(data, start, mid - 1, target)

for i in range(m):
  if binarySearch(dataN, 0, n-1, dataM[i]):
    result.append("yes")
  else:
    result.append("no")

  print(result[i], end=" ")

  

  
  

