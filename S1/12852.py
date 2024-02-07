n = int(input())
dp_cnt = {1:0}
dp_path = {1:[1]}

for i in range(2, n+1):
  dp_cnt[i] = dp_cnt[i-1]+1
  path = i-1
  
  if i % 3 == 0 and dp_cnt[i//3]+1 < dp_cnt[i]:
    dp_cnt[i] = dp_cnt[i//3]+1
    path = i//3
    
  if i % 2 == 0 and dp_cnt[i//2]+1 < dp_cnt[i]:
    dp_cnt[i] = dp_cnt[i//2]+1
    path = i//2
  
  dp_path[i] = [i] + dp_path[path]

print(dp_cnt[n])
print(*dp_path[n])