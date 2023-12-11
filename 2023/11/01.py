with open("i") as f:
  t = f.read().strip().split("\n")

exp_r = set()
exp_c = set()
gal = []

for y, r in enumerate(t):
  if all(i == "." for i in r):
    exp_r.add(y)
  for x, g in enumerate(r):
    if y == 0:
      if all(t[i][x] == "." for i in range(len(t))):
        exp_c.add(x)
    if g == "#":
      gal.append((x, y))

path = 0

for off, (x1, y1) in enumerate(gal):
  for x2, y2 in gal[off + 1:]:
    add = 0
    for i in exp_r:
      if i in range(y1, y2):
        add += 1
    for i in exp_c:
      if i in range(*sorted([x1, x2])):
        add += 1
    p = abs(x2 - x1) + abs(y2 - y1) + add
    path += p

print(path)
