q = int(input())

for _ in range(q):
  ta, tb, va, vb = map(int, input().split())
  time = tb*vb
  va -= time // ta
  if va < 0: pass
  elif time % ta == 0:
    if va % 2 == 1:
      time += (va-1)*ta//2 + ta
    else:
      time += va*ta//2
  else:
    도훈_start = time % ta
    while va != 0:
      time += 1
      if time % ta == 0:
        va -= 1
      elif time % ta == 도훈_start:
        va -= 1
  
  print(time)