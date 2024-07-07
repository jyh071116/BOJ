x = int(input())
if x == 1:
  print("1/1")
  exit()
n = 1
i = 1
j = 2
up_or_down = "down"
while True:
  if up_or_down == "down":
    while j != 0:
      n += 1
      if n == x:
        print(f"{i}/{j}")
        exit()
      i += 1
      j -= 1
    up_or_down = "up"
    j += 1
  else:
    while i != 0:
      n += 1
      if n == x:
        print(f"{i}/{j}")
        exit()
      i -= 1
      j += 1
    up_or_down = "down"
    i += 1