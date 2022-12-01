with open("i") as f:
  m = [i.split("-") for i in map(str.strip, f.readlines())]
  n = { }
  for a, b in m:
    if a not in n:
      n[a] = []
    n[a].append(b)
    if b not in n:
      n[b] = []
    n[b].append(a)

def visit(d = "start", v = [], t = False):
  s = 0
  for i in n[d]:
    if i == "start": continue
    elif i == "end": s += 1
    else:
      if i in v and i.islower():
        if t: continue
        s += visit(i, [*v, d], True)
      else:
        s += visit(i, [*v, d], t)
  return s

print(visit())