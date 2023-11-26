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

print(sides)