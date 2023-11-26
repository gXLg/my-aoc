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

mx = 4_000_000
#mx = 20
pos = set()

for i, (b, c) in enumerate(mapp):
  man = mann[(b, c)]
  for j in range(- man - 1, man + 2):
    d = b + j
    if not (0 <= d <= mx): continue
    f = man + 1 - abs(j)
    g, h = c + f, c - f
    fg = 0 <= g <= mx
    fh = 0 <= h <= mx
    for k, l in mapp:
      if fg:
        if abs(k - d) + abs(l - g) <= mann[(k, l)]:
          fg = False
      if fh:
        if abs(k - d) + abs(l - h) <= mann[(k, l)]:
          fh = False
      if not (fg or fh): break
    if fg: pos.add((d, g))
    if fh: pos.add((d, h))
    if pos: break

a, b = [*pos][0]
print(a * 4_000_000 + b)
