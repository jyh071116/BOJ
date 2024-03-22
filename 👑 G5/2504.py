n = input()
stack = []
res = []
i = 0
while i < len(n):
  if i < len(n)-1 and n[i] == "(" and n[i+1] == ")":
    res.append(2)
    i += 1
  elif i < len(n)-1 and n[i] == "[" and n[i+1] == "]":
    res.append(3)
    i += 1
  elif n[i] == "(":
    stack.append(("(", len(res)))
  elif n[i] == "[":
    stack.append(("[", len(res)))
  elif n[i] == ")":
    if len(stack) == 0 or stack[-1][0] != "(":
      print(0)
      exit()
    else:
      temp = stack.pop()
      for j in range(temp[1], len(res)):
        res[j] *= 2
  elif n[i] == "]":
    if len(stack) == 0 or stack[-1][0] != "[":
      print(0)
      exit()
    else:
      temp = stack.pop()
      for j in range(temp[1], len(res)):
        res[j] *= 3
  i += 1
  
if not stack:
  print(sum(res))
else:
  print(0)