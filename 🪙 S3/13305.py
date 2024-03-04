n = int(input())
paths = list(map(int, input().split()))
costs = list(map(int, input().split()))

min_cost = float('inf')
res = 0

for i in range(n-1):
  if costs[i] < min_cost:
    min_cost = costs[i]
  res += min_cost*paths[i]
  
print(res)