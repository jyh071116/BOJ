n = int(input())
arr = [int(input()) for _ in range(n)]

def gcd(a, b):
  if a % b == 0: return b
  return gcd(b, a%b)

diff = []
for i in range(n-1):
  diff.append(abs(arr[i]-arr[i+1]))

diff_gcd = diff[-1]
for i in range(len(diff)-1):
  diff_gcd = gcd(diff_gcd, diff[i])

for i in range(2, diff_gcd+1):
  if diff_gcd % i == 0:
    print(i, end=" ")