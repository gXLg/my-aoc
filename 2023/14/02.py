with open("i") as f:
  t = f.read().strip().split("\n")

#steady = set()
#loose = set()

mapp = []

for y, l in enumerate(t):
  mapp.append([])
  for x, stone in enumerate(l):
    #cords = complex(x, y)
    if stone == "#":
      mapp[-1].append(1)
      #steady.add(cords)
    elif stone == "O":
      mapp[-1].append(2)
      #loose.add(cords)
    else:
      mapp[-1].append(0)

loop = []

for rr in range(1000000000):

  # NORTH
  for column in range(len(t[0])):
    before = 0
    air = 0
    after = []
    for i in range(len(t)):
      c = mapp[i][column]
      if c == 2:
        before += 1
      elif c == 0:
        air += 1
      else:
        after.extend([2] * before + [0] * air + [1])
        air = 0
        before = 0
    after.extend([2] * before + [0] * air)


    for j, c in enumerate(after):
      mapp[j][column] = c

  # WEST (left)
  for y, line in enumerate(mapp):
    before = 0
    air = 0
    after = []
    for c in line:
      if c == 2:
        before += 1
      elif c == 0:
        air += 1
      else:
        after.extend([2] * before + [0] * air + [1])
        air = 0
        before = 0
    after.extend([2] * before + [0] * air)

    mapp[y] = after

  # SOUTH
  for column in range(len(t[0])):
    before = 0
    air = 0
    after = []
    for i in range(len(t))[::-1]:
      c = mapp[i][column]
      if c == 2:
        before += 1
      elif c == 0:
        air += 1
      else:
        after.extend([2] * before + [0] * air + [1])
        air = 0
        before = 0
    after.extend([2] * before + [0] * air)

    for j, c in enumerate(after[::-1]):
      mapp[j][column] = c

  # EAST
  for y, line in enumerate(mapp):
    before = 0
    air = 0
    after = []
    for c in line[::-1]:
      if c == 2:
        before += 1
      elif c == 0:
        air += 1
      else:
        after.extend([2] * before + [0] * air + [1])
        air = 0
        before = 0
    after.extend([2] * before + [0] * air)

    mapp[y] = after[::-1]

  unique = tuple(tuple(j) for j in mapp)
  if unique in loop:
    fi = loop.index(unique)
    break
  loop.append(unique)

su = 0
for y, line in enumerate(loop[(1000000000 - fi) % (rr - fi) + (fi - 1)]):
  su += line.count(2) * (len(t) - y)

print(su)

#  sum = 0
#print(int(sum))
#  sum += len(t) - stone.imag
