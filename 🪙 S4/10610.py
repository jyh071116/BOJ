n = list(input())
n.sort(reverse=True)
if n[-1] == '0' and sum(map(int, n)) % 3 == 0:
  print("".join(n))
else:
  print(-1)