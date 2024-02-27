n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_cnt = {"black": 0, "white": 0}
possible = {"black": [], "white": []}
for i in range(n):
  for j in range(n):
    if arr[i][j] == 1 and (i+j)%2 == 0:
      possible["black"].append([i, j, 1])
    elif arr[i][j] == 1 and (i+j)%2 == 1:
      possible["white"].append([i, j, 1])
length = {"black": len(possible["black"]), "white": len(possible["white"])}
ans = []

def backtracking(index, cnt, color):
  global max_cnt
  
  if length[color] == index:
    max_cnt[color] = max(max_cnt[color], cnt)
    return
  
  x, y, is_possible = possible[color][index]
  
  if is_possible != 1:
    return backtracking(index+1, cnt, color)
  
  temp = []
  for i in range(length[color]):
    a, b, posi = possible[color][i]
    if x+y == a+b or x-y == a-b:
      possible[color][i][2] -= 1
      temp.append(i)
  backtracking(index+1, cnt+1, color)
  
  for i in temp:
    possible[color][i][2] += 1
  backtracking(index+1, cnt, color)

backtracking(0, 0, "black")
backtracking(0, 0, "white")
print(max_cnt["black"] + max_cnt["white"])