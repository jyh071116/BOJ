n = int(input())
arr = list(map(int, input().split()))
arr.sort()

close = [arr[0], arr[1], arr[n-1]]
for std in range(n-2):
  start = std+1
  end = n-1
  while start < end:
    sum = arr[std]+arr[start]+arr[end]
    if abs(sum) < abs(close[0]+close[1]+close[2]):
      close = [arr[std], arr[start], arr[end]]
    
    if sum > 0:
      end -= 1
    elif sum < 0:
      start += 1
    else:
      break

print(*close)