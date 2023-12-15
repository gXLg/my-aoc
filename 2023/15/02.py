with open("i") as f:
  l = f.read().strip().split(",")

def hhash(i):
  v = 0
  for j in i:
    v = (v + ord(j)) * 17 % 256
  return v

boxs = [[] for i in range(256)]

for i in l:
  if "=" in i:
    a, b = i.split("=")
    h = hhash(a)
    idx = -1
    for j, bo in enumerate(boxs[h]):
      if bo[0] == a:
        idx = j
        break

    if idx == -1: boxs[h].append([])
    boxs[h][idx] = [a, int(b)]

  else:
    a = i[:-1]
    h = hhash(a)
    idx = -1
    for j, b in enumerate(boxs[h]):
      if b[0] == a:
        idx = j
        break
    if ~idx:
      boxs[h].pop(idx)

s = 0
for i, b in enumerate(boxs):
  for j, v in enumerate(b):
    s += (i + 1) * (j + 1) * v[1]

print(s)
