with open("i") as f:
  t = f.read().strip().split()

stars = { }

for y, line in enumerate(t):
  current = ""
  start = None
  for x, sym in enumerate(line):
    if sym in "0123456789":
      current += sym
      if start is None:
        start = x

    if (x == len(line) - 1 or sym not in "0123456789") and current:

      if start > 0: xl = 1
      else: xl = 0

      if start + len(current) < len(line): xr = 1
      else: xr = 0

      xen = len(current) + xl + xr

      flag = True
      if y > 0:
        adj = t[y - 1][start - xl:start + len(current) + xr]
        if adj != "." * xen:
          if "*" in adj:
            c = (y - 1, start - xl + adj.find("*"))
            if c in stars: stars[c].append(current)
            else: stars[c] = [current]
          flag = False
      if y + 1 < len(t):
        adj = t[y + 1][start - xl:start + len(current) + xr]
        if adj != "." * xen:
          if "*" in adj:
            c = (y + 1, start - xl + adj.find("*"))
            if c in stars: stars[c].append(current)
            else: stars[c] = [current]
          flag = False
      if start > 0:
        if line[start - 1] != ".":
          flag = False
        if line[start - 1] == "*":
          c = (y, start - xl)
          if c in stars: stars[c].append(current)
          else: stars[c] = [current]
      if start + len(current) < len(line):
        if line[start + len(current)] != ".":
          flag = False
        if line[start + len(current)] == "*":
          c = (y, start + len(current))
          if c in stars: stars[c].append(current)
          else: stars[c] = [current]

      current = ""
      start = None

s = 0
for c in stars:
  try:
    a, b = map(int, stars[c])
    s += a * b
  except: pass

print(s)
