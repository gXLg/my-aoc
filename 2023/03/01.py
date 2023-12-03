with open("i") as f:
  t = f.read().strip().split()

s = 0
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
          flag = False
      if y + 1 < len(t):
        adj = t[y + 1][start - xl:start + len(current) + xr]
        if adj != "." * xen:
          flag = False
      if start > 0:
        if line[start - 1] != ".":
          flag = False
      if start + len(current) < len(line):
        if line[start + len(current)] != ".":
          flag = False

      if not flag:
        s += int(current)

      current = ""
      start = None

print(s)
