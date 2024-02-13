import math

a, b, c = map(int, input().split())
start, end = 0, 10**6

while abs(end-start) >= 10**(-9):
  mid = (start + end) / 2
  
  val = a*mid + b*math.sin(mid)
  
  if val >= c:
    end = mid
  else:
    start = mid

print(mid)