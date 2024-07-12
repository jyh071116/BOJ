sdoku = [list(input()) for _ in range(9)]

def backtraking(a, b):
  global sdoku
  if a >= 9:
    for i in sdoku:
      for j in i:
        print(j, end="")
      print()
    exit()
  if b == 9: return backtraking(a+1, 0)
  if sdoku[a][b] != '0': return backtraking(a, b+1)
  
  for i in range(1, 10):
    if str(i) not in sdoku[a] and str(i) not in [sdoku[row][b] for row in range(9)]:
      if str(i) not in set(sum([sdoku[row][b//3*3:b//3*3+3] for row in range(9) if a//3*3 <= row < a//3*3+3], [])):
        sdoku[a][b] = str(i)
        backtraking(a, b+1)
        sdoku[a][b] = '0'

backtraking(0, 0)