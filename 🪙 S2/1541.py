arr = input()
if "-" in arr:
  arr = arr.split('-')
  res = 0
  for i in range(len(arr)):
    if "+" in arr[i]:
      arr[i] = sum(map(int, arr[i].split('+')))
    
    if i == 0:
      res += int(arr[i])
    else:
      res -= int(arr[i])
  print(res)
else:
  print(sum(map(int, arr.split('+'))))