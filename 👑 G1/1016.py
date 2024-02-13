min, max = map(int, input().split())
제곱ㅇㅇ수 = {}

cnt = max-min+1
i = 2
while i*i <= max:
  val = min // (i*i)
  if val*(i*i) < min: val += 1
  
  while val*(i*i) <= max:
    if val*(i*i) not in 제곱ㅇㅇ수:
      제곱ㅇㅇ수[val*(i*i)] = 1
      cnt -= 1
    val += 1
  
  i += 1

print(cnt)