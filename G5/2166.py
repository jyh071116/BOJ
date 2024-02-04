n = int(input())
dots = [list(map(int, input().split())) for _ in range(n)]

area = 0
j = n-1
for i in range(n):
  area += (dots[j][0] + dots[i][0])*(dots[j][1] - dots[i][1])
  j = i

print(round(abs(area/2), 1))