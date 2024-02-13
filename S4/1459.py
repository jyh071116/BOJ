x, y, w, s = map(int, input().split())

if w*2 <= s:
  print((x+y)*w)
else:
  a, b, c = float('inf'), float('inf'), float('inf')
  
  if (x + y) % 2 == 0:
    a = max(x, y)*s
    
  else:
    b = (max(x, y)-1)*s + w
    
  c = min(x, y)*s + abs(x-y)*w
  
  print(min(a, b, c))