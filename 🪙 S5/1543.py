word = input()
find = input()
cnt = 0
visited_max = -1

for i in range(len(word)):
  if i <= visited_max:
    continue
  
  if word[i] == find[0]:
    for j in range(len(find)):
      if i+j >= len(word):
        break
      if word[i+j] != find[j]:
        break
    else:
      cnt += 1
      visited_max = i+j

print(cnt)