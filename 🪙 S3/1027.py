x, y = map(int, input().split())
z = int(y*100/x)
start, end = 0, 10**9 + x
while start < end:
  mid = (start + end)//2
  percent = int((y+mid)*100/(x+mid))
  if percent == z:
    start = mid + 1
  elif percent > z:
    end = mid

if percent == z and end == 10**9+x:
  print(-1)
else:
  print(end)