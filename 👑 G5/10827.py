from decimal import Decimal, getcontext
getcontext().prec = 10000

def power(a: Decimal, b):
  if b == 1:
    return a
  temp = power(a, b//2)
  if b % 2 == 0:
    return temp * temp
  elif b % 2 == 1:
    return a * temp * temp

a, b = input().split()
print(f'{power(Decimal(a), int(b)):f}')