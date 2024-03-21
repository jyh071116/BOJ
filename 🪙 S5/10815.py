n = int(input())
dic = {}
for i in map(int, input().split()):
  dic[i] = 1
m = int(input())
for i in map(int, input().split()):
  if dic.get(i):
    print(1, end=" ")
  else:
    print(0, end=" ")