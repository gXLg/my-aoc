with open("i") as f:
  l = f.read().strip().split(",")

s = 0
for i in l:
  v = 0
  for j in i:
    v = (v + ord(j)) * 17 % 256
  s += v

print(s)
