n, s, r = map(int, input().split())
kayak = [1]*(n+1)
kayak[0] = 0

for i in map(int, input().split()):
  kayak[i] -= 1

for i in map(int, input().split()):
  kayak[i] += 1

for i in range(1, n+1):
  if kayak[i] == 0:
    try:
      if kayak[i-1] == 2:
        kayak[i-1] -= 1
        kayak[i] += 1
      elif kayak[i+1] == 2:
        kayak[i+1] -= 1
        kayak[i] += 1
    except:
      pass

print(len([i for i in kayak if i == 0])-1)