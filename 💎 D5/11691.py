n = int(input())
res = 0
mod = 1000000007

sp = [0]*(n+1)
prime = []
my = [0]*(n+1)
my[1] = 1

for i in range(2, n+1):
  if not sp[i]:
    prime.append(i)
    my[i] = i - i*i
  for j in prime:
    if i*j > n: break
    sp[i*j] = j
    if i%j == 0:
      my[i*j] = my[i]*j
      break
    my[i*j] = my[i] * my[j]


for i in range(1, n+1):
  n_divided_i = n//i
  res += ((((n_divided_i)*((n_divided_i)+1)//2)**2) * my[i])

print((res-((n*(n+1))//2))//2 % mod)