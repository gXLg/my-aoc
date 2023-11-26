with open("t") as f:
  b, moves = f.read().strip("\n").split("\n\n")

look = " .#"
empt = set()
free = set()
wall = set()
lx = max(map(len, b.split("\n")))
first = True
for y, row in enumerate(b.split("\n")):
  bb = row + (lx - len(row)) * " "

  for x, r in enumerate(row):
    i = look.index(r)
    match i:
      case 0:
        empt.add(x + y * 1j)
      case 1:
        free.add(x + y * 1j)
        if first:
          first = False
          walker = x + 0j
      case 2:
        wall.add(x + y * 1j)

mov = [1, 1j, -1, -1j]
cur = 0

ly = len(b.split("\n"))

size = 4
xx, yy = lx // size, ly // size
net = set()
for y in range(0, ly, size):
  for x in range(0, lx, size):
    if x + y * 1j in wall.union(free):
      net.add(x // size + y // size * 1j)

outline = set()

for n in net:
  for i in mov:
    if (n + i) not in net:
      outline.add(n + i)

peri = []
p = [*outline][0]
for i in mov:
  if p + i in net:
    peri.append((p + i, - i))
    break

# cube net perimeter
while len(peri) < 14:
  n, i = peri[-1]
  for m in net:
    f = False
    for j in mov:
      if (
        (
          abs((m + j) - (n + i)) <= 1
          or
          (
            m == n
            and
            abs((m + j) - (n + i)) < 2
          )
        )
        and
        abs(m - n) < 2
        and
        (m + j) in outline
        and
        (m, j) not in peri
      ):
        f = True
        peri.append((m, j))
        break
    if f: break

toge = { }
for p in range(len(peri)):
  q, r = (peri + [peri[0]])[p:p + 2]
  if 1 < abs(q[0] - r[0]) < 2:
    toge[q] = r
    toge[r] = q
    break

#print(toge)
#print(len(peri))
#exit()

pl, pr = p, p + 1
for i in range(6):
  pl = (pl - 1) % 14
  pr = (pr + 1) % 14
  q, r = peri[pl], peri[pr]
  toge[q] = r
  toge[r] = q

#print(toge[(2 + 1j, 1)])
print(toge)
exit()

import re
for i in re.findall("\d+|[RL]", moves):
  if i == "R":
    cur = (cur + 1) % 4
  elif i == "L":
    cur = (cur - 1) % 4
  else:
    for j in range(int(i)):
      print(walker)
      input()
      n = walker + mov[cur]
      if n in free:
        walker = n
      elif n in wall:
        break
      else:
        re, im = walker.real, walker.imag
        mi = re // size + im // size * 1j
        ne, s = toge[(mi, mov[cur])]
        of = (re % size) + (im % size) * 1j
        of -= mov[cur] * (size - 1)

        d = mov.index(s)
        rot = (- d - cur) % 4

        print("gonna rotate", rot, of, cur)

        mid = (1 + 1j) * (size - 1) / 2
        for k in range(rot):
          of = (of - mid) / 1j + mid
          print(of, k)

        n = ne * size + of
        if n in wall: break

        walker = n
        cur = (d) % 4

        #m = mov[(cur + 2) % 4]
        #p = walker
        #while True:
        #  if p + m not in wall and p + m not in free:
        #    break
        #  p += m
        #if p in wall:
        #  break
        #walker = p

print(int(
  (walker.imag + 1) * 1000 +
  (walker.real + 1) * 4 + (cur + 1)
))
print(walker.imag, walker.real, cur)
