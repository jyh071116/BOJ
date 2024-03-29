import sys
input = sys.stdin.readline

while True:
  n, m = map(int, input().split())
  if n == 0 and m == 0:
    break
  cnt = 0
  dic = {}
  for _ in range(n):
    dic[int(input())] = 1
  for _ in range(m):
    temp = int(input())
    if dic.get(temp):
      dic[temp] += 1

  for i in dic.keys():
    if dic[i] == 2:
      cnt += 1
  print(cnt)