n, m = map(int, input().split())
woods = list(map(int, input().split()))
start = 0 
end = sum(woods)

while start <= end:
  mid = (start + end) // 2
  my_wood = 0
  for wood in woods:
    if wood > mid:
      my_wood += wood - mid
  
  if my_wood >= m:
    start = mid+1
  else:
    end = mid-1
  
print(end)