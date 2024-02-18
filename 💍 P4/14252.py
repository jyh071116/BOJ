n = int(input())
arr =list(map(int, input().split()))
arr.sort()

cnt = 0

def gcd(a, b):
  if a % b == 0: return b
  return gcd(b, a%b)

for i in range(n-1):
  if gcd(arr[i], arr[i+1]) != 1:
    for j in range(arr[i]+1, arr[i+1]):
      if gcd(arr[i], j) == 1 and gcd(arr[i+1], j) == 1:
        cnt += 1
        break
    else:
      cnt += 2

print(cnt)