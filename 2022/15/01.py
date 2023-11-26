with open("i") as f:
  l = f.read().strip().split("\n")

mapp = { }
mann = { }

for i in l:
  a, b, c, d, e = i.split("=")
  b = int(b.split(",")[0])
  c = int(c.split(":")[0])
  d = int(d.split(",")[0])
  e = int(e)
  man = abs(b - d) + abs(c - e)

  mapp[(b, c)] = (d, e)
  mann[(b, c)] = man

y = 2_000_000
ys = set()

for b, c in mapp:
  r = max(mann[(b, c)] - abs(c - y), 0)
  ys.update(range(b - r, b + r + 1))

for d, e in mapp.values():
  if e == y:
    ys.discard(d)

print(len(ys))

#y = 2_000_000
#s = 0
#for x in range(minx, maxx + 1):
#  f = False
#  for b, c in mapp:
#    d, e = mapp[(b, c)]
#    if (d, e) == (x, y):
#      break
#    mani = abs(b - d) + abs(c - e)
#    manf = abs(b - x) + abs(c - y)
#    if manf <= mani:
#      f = True
#      break
#  if f: s += 1
#
#print(s)
