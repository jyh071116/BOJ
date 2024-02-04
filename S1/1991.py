n = int(input())
dic = {}
for i in range(1, n+1):
  node, left, right = input().split()
  dic[node] = [left, right]

def preorder(node):
  if node == ".":
    return
  print(node, end="")
  preorder(dic[node][0])
  preorder(dic[node][1])

def inorder(node):
  if node == ".":
    return
  inorder(dic[node][0])
  print(node, end="")
  inorder(dic[node][1])

def postorder(node):
  if node == ".":
    return
  postorder(dic[node][0])
  postorder(dic[node][1])
  print(node, end="")

preorder('A')
print()
inorder('A')
print()
postorder('A')