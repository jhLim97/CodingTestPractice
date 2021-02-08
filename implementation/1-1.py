n = int(input())
data = input().split()

x, y = 1, 1

'''
방법 1. jhLim
for i in range(len(data)):
  if data[i] == 'L':
    if y-1 >= 1:
      y -= 1
  elif data[i] == 'R':
    if y+1 <= n:
      y += 1
  elif data[i] == 'U':
    if x-1 >= 1:
      x -= 1
  else:
    if x+1 <= n:
      x += 1
'''
# 방법 2. test
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for i in data:
  for j in range(len(move_types)):
    if i == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  
  x, y = nx, ny

print(x, y) 