n = input()
cnt = len(n)
for i in range(len(n)-1):
  if n[i] == "c":
    if n[i+1] == "=" or n[i+1] == "-":
      cnt -= 1
  elif n[i] == "d":
    try:
      if n[i+1] == "z" and n[i+2] == "=" or n[i+1] == "-":
        cnt -= 1
    except:
      if n[i+1] == "-":
        cnt -= 1
  elif n[i] == "l" and n[i+1] == "j":
    cnt -= 1
  elif n[i] == "n" and n[i+1] == "j":
    cnt -= 1
  elif n[i] == "s" and n[i+1] == "=":
    cnt -= 1
  elif n[i] == "z" and n[i+1] == "=":
    cnt -= 1

print(cnt)