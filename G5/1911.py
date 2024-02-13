import math

n, l = map(int, input().split())
pool = [list(map(int, input().split())) for _ in range(n)]
pool.sort(key=lambda x:x[0])
plank = 0
next = 0

for i in range(n):
  start, end = pool[i]
  if next > 0:
    start += next
  
  now_plank = math.ceil((end-start)/l)
  plank += now_plank
  
  try:
    next = (start + l*now_plank) - pool[i+1][0]
  except:
    break

print(plank)