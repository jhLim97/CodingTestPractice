n = int(input())

cnt = 0

'''
방법 1. jhLim97
h,m,s = 0,0,0 
while True:

  m, s = 0, 0
  if h==n+1:
    break

  if h == 3:
    cnt += 3600
    h += 1
    continue
  else:
    for m in range(60):
      if m%10 == 3 or m//10 == 3:
        cnt +=60
        continue
      else:
        for s in range(60):
          if s%10 == 3 or s//10 == 3:
            cnt += 1
            continue
    h += 1
'''
# 방법 2. test
for i in range(n+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i)+str(j)+str(k):
        cnt += 1

print(cnt)


