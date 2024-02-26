l, c = map(int, input().split())
letters = list(input().split())
letters.sort()

def f(cipher, last):
  if len(cipher) == l:
    모음cnt = 0
    for i in ['a', 'e', 'i', 'o', 'u']:
      모음cnt += list(cipher).count(i)
    if 모음cnt >= 1 and l-모음cnt >= 2:
      print(cipher)
    return
  
  for i in range(last+1, c):
    f(cipher + letters[i], i)

f('', -1)