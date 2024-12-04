with open("i") as f:
  l = f.read().strip().split("\n")

comp = { }
def put(a, b):
  if a not in comp:
    comp[a] = set()
  comp[a].add(b)
  if b not in comp:
    comp[b] = set()
  comp[b].add(a)

for i in l:
  a, b = i.split(": ")
  for j in b.split():
    put(a, j)

groups = [{ [*comp.keys()][0] }]
while groups:
  n = []

  for group in groups:
    # group connections
    c = 0
    for i in group:
      c += len(comp[i] - group)
    if c == 3:
      print("FOUND!!1!")
      print(len(group), len(comp.keys()) - len(group))
      exit()

    for i in group:
      for j in comp[i]:
        if j in group: continue
        g = group | {j}
        if not g in n:
          n.append(g)

  groups = n
  print(len(groups))
