import sys
import math
from decimal import Decimal, getcontext
input = sys.stdin.readline
getcontext().prec = 1000
t = int(input())
for _ in range(t):
  n = Decimal(input().strip())
  res = n**(Decimal('1')/Decimal('3'))
  res = round(res, 500)
  print(math.floor(res * Decimal('1e10'))/Decimal('1e10'))