n = int(input())
arr = list(map(int, input().split()))
arr = [0] + arr
dp = [0]*(n+1)
dp_len = 1

def binary_search(start, end, key):
  mid = (start+end)//2
  if start > end:
    return -1
  if dp[mid] < key <= dp[mid+1]:
    return mid+1
  if dp[mid] >= key:
    return binary_search(start, mid-1, key)
  if dp[mid] < key:
    return binary_search(mid+1, end, key)
  

for i in range(1, n+1):
  index = binary_search(0, dp_len-1, arr[i])
  
  if index == -1:
    dp[dp_len] = arr[i]
    dp_len += 1
  else:
    dp[index] = arr[i]

print(dp_len - 1)