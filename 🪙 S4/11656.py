s = input()
arr = sorted([s[i:] for i in range(len(s))])
for i in arr:
  print(i)