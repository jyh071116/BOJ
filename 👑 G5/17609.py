import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = input().strip()
  유사회문 = False
  p0, p1 = 0, len(n)-1
  while p0 < p1:
    if n[p0] == n[p1]:
      p0 += 1
      p1 -= 1
      continue
    if n[p0] != n[p1]:
      if 유사회문:
        print(2)
        break
      else:
        if n[p0+1] == n[p1] and n[p0] == n[p1-1]:
          p0 += 1
          p1 -= 1
          if p0 > p1:
            print(1)
            break
        elif n[p0+1] == n[p1]:
          유사회문 = True
          p0 += 1
        elif n[p0] == n[p1-1]:
          유사회문 = True
          p1 -= 1
        else:
          print(2)
          break
        
  else:
    if 유사회문:
      print(1)
    else:
      print(0)