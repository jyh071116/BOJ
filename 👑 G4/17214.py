n = input()
try:
  idx = n.index("x")
  start = str(int(n[:idx])//2)
  end = n[idx+1:]
  if start == "1":
    start = ""
  elif start == "-1":
    start = "-"
  
  if end == "+1":
    end = "+"
  elif end == "-1":
    end = "-"
    
  if end == "0" or len(end) == 0:
    print(start + "xx+" + "W")
  else:
    print(start + "xx" + end + "x+" + "W")
except:
  if n == "0":
    print("W")
  elif n == "1":
    print("x+W")
  elif n == "-1":
    print("-x+W")
  else:
    print(n+"x+"+"W")