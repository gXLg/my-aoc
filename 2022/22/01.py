with open("i") as f:
  b, moves = f.read().strip("\n").split("\n\n")

look = " .#"
empt = set()
free = set()
wall = set()
l = max(map(len, b.split("\n")))
first = True
for y, row in enumerate(b.split("\n"), start = 1):
  bb = row + (l - len(row)) * " "

  for x, r in enumerate(row, start = 1):
    i = look.index(r)
    match i:
      case 0:
        empt.add(x + y * 1j)
      case 1:
        free.add(x + y * 1j)
        if first:
          first = False
          walker = x + 1j
      case 2:
        wall.add(x + y * 1j)

mov = [1, 1j, -1, -1j]
cur = 0

import re
for i in re.findall("\d+|[RL]", moves):
  if i == "R":
    cur = (cur + 1) % 4
  elif i == "L":
    cur = (cur - 1) % 4
  else:
    for j in range(int(i)):
      n = walker + mov[cur]
      if n in free:
        walker = n
      elif n in wall:
        break
      else:
        m = mov[(cur + 2) % 4]
        p = walker
        while True:
          if p + m not in wall and p + m not in free:
            break
          p += m
        if p in wall:
          break
        walker = p

print(int(walker.imag * 1000 + walker.real * 4 + cur))
#print(walker.imag, walker.real, cur)