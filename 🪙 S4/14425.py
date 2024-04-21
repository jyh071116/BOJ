n, m = map(int, input().split())
dic = {}
for _ in range(n):
  dic[input()] = 1

cnt = 0
for _ in range(m):
  if dic.get(input()):
    cnt += 1

print(cnt)