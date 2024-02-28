n = int(input())
p = list(map(int, input().split()))
grundy = p[-1]
for i in range(n-1):
  grundy = grundy ^ p[i]
if grundy == 0:
  print("cubelover")
else:
  print("koosaga")