n = input()
res = [0]*len(n)
i = 0
while i < len(n):
  if n[i] == ".":
    res[i] = "."
    i += 1
  elif i <= len(n)-4 and n[i:i+4] == "XXXX":
    for j in range(i, i+4):
      res[j] = "A"
    i += 4
  elif i <= len(n)-2 and n[i:i+2] == "XX":
    for j in range(i, i+2):
      res[j] = "B"
    i += 2
  else:
    print(-1)
    exit()

print("".join(res))