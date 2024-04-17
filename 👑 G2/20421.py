m, seed, x1, x2 = map(int, input().split())
a = (x2 - x1) * pow(x1-seed, m-2, m) % m
c = (x1 - a*seed) % m
print(a, c)