from queue import PriorityQueue

n = int(input())
q = PriorityQueue()

for _ in range(n):
  i = int(input())
  q.put(i)

cnt = 0
while q.qsize() != 1:
  try:
    temp = q.get() + q.get()
    q.put(temp)
    cnt += temp
  except:
    pass

print(cnt)