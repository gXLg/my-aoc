with open("i") as f:
  m = f.read().strip().split("\n")

def count(start):
  cords = set()
  covered = set()
  beams = [start]

  while beams:
    nextb = []
    for pos, dir in beams:
      where = pos + dir
      x, y = where.real, where.imag
      wo = where

      if x not in range(len(m[0])) or y not in range(len(m)):
        continue

      char = m[int(y)][int(x)]

      if not dir.real: # vertical |
        if char in ".|":
          end = [dir]
        elif char == "-":
          end = [1, -1]
        elif char == "/":
          if dir == 1j:
            end = [-1]
          else:
            end = [1]
        elif char == "\\":
          if dir == 1j:
            end = [1]
          else:
            end = [-1]

      else:
        if char in ".-":
          end = [dir]
        elif char == "|":
          end = [1j, -1j]
        elif char == "/":
          if dir == 1:
            end = [-1j]
          else:
            end = [1j]
        elif char == "\\":
          if dir == 1:
            end = [1j]
          else:
            end = [-1j]

      for d in end:
        if (where, d) in covered: continue
        covered.add((where, d))
        nextb.append((where, d))
        cords.add(where)

    beams = nextb

  return len(cords)

res = []

for y in range(len(m)):
  for x, d in [(-1, 1), (len(m[0]), -1)]:
    res.append(count((x + y * 1j, d)))

for y, d in [(-1, 1j), (len(m), -1j)]:
  for x in range(len(m[0])):
    res.append(count((x + y * 1j, d)))

print(max(res))
