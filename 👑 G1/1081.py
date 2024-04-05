l, u = map(int, input().split())

def getSum(n):
  _sum = 0
  previous = []
  while n != 0:
    length = len(str(n))
    remain = int(str(n)[0]) % 10
    _sum += int(45*(10**(length-2))*remain*(length-1))
    _sum += ((remain-1)*remain//2)*10**(length-1)
    _sum += remain
    _sum += sum([j*10**(length-1)*remain for j in previous])
    previous.append(remain)
    n = int(str(n)[1:] or '0')
  return _sum
    
print(getSum(u) - getSum(0 if l-1 == -1 else l-1))