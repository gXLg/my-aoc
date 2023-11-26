with open("i") as f:
  cuc = [[*map(int, i.split(","))] for i in f.read().strip().split("\n")]
  cu = { (a, b, c) for a, b, c in cuc }

sides = 6 * len(cu)

for xx, yy, zz in cu:
  for dx, dy, dz in [
    [-1, 0, 0],
    [1, 0, 0],
    [0, -1, 0],
    [0, 1, 0],
    [0, 0, -1],
    [0, 0, 1]
  ]:
    new = (xx + dx, yy + dy, zz + dz)
    if new in cu:
      sides -= 1

Mx, My, Mz = [0] * 3
mx, my, mz = [99999999] * 3
for a, b, c in cu:
  if a > Mx: Mx = a
  if b > My: My = b
  if c > Mz: Mz = c

  if a < mx: mx = a
  if b < my: my = b
  if c < mz: mz = c


volume = set()
for x in range(mx - 1, Mx + 2):
  for y in range(my - 1, My + 2):
    for z in range(mz - 1, Mz + 2):
      volume.add((x, y, z))

for i in cu:
  volume.discard(i)

x, y, z = mx - 1, my - 1, mz - 1
volume.discard((x, y, z))

flag = True
air = False
adj = [(x, y, z)]
i = 0
while flag:
  flag = False
  for xx, yy, zz in adj[i:]:
    for dx, dy, dz in [
      [-1, 0, 0],
      [1, 0, 0],
      [0, -1, 0],
      [0, 1, 0],
      [0, 0, -1],
      [0, 0, 1]
    ]:
      new = (xx + dx, yy + dy, zz + dz)
      if not new in adj:
        if new in volume:
          adj.append(new)
          volume.remove(new)
          flag = True
    i += 1

inside = 0
n = [*volume]
while n:
  x, y, z = n.pop()

  flag = True
  air = False
  adj = [(x, y, z)]
  i = 0
  a = 0
  while flag:
    flag = False
    for xx, yy, zz in adj[i:]:
      for dx, dy, dz in [
        [-1, 0, 0],
        [1, 0, 0],
        [0, -1, 0],
        [0, 1, 0],
        [0, 0, -1],
        [0, 0, 1]
      ]:
        new = (xx + dx, yy + dy, zz + dz)
        if not new in adj:
          if new in n:
            adj.append(new)
            n.remove(new)
            flag = True
          else:
            a += 1
      i += 1


  if not air:
    #print("bubble with", len(adj), "has area", a)
    inside += a

print(sides - inside)