a, b = map(int, input().split())
sum = 0
i = 1
while i <= b:
  j = b//(b//i)
  sum += (i+j)*(b//i)*(j-i+1)//2
  i = j+1


i = 1
while i <= a-1:
  j = (a-1)//((a-1)//i)
  sum -= (i+j)*((a-1)//i)*(j-i+1)//2
  i = j+1

print(sum)