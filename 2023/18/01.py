with open("i") as f:
  r = f.read().strip().split("\n")

cords = 0 + 0j
edges = set()

mx = my = mix = miy = 0

for l in r:
  a, b, c = l.split()
  dir = { "R": 1, "L": -1, "U": -1j, "D": 1j }[a]
  num = int(b)

  co = cords + dir * num
  #x.append(int(co.real))
  #y.append(int(co.imag))
  #cor.append([int(cords.real) + 2, int(cords.imag) + 1])
  edges.add((co, cords))
  cords = co

  if cords.imag > my:
    my = int(cords.imag)
  if cords.real > mx:
    mx = int(cords.real)
  if cords.imag < miy:
    miy = int(cords.imag)
  if cords.real < mix:
    mix = int(cords.real)

#
#def ra(a, b, x, y):
#  xx, xxx = map(int, sorted([a.real, b.real]))
#  yy, yyy = map(int, sorted([a.imag, b.imag]))
#  return x in range(xx, xxx + 1) and y in range(yy, yyy + 1)
#
#print(my - miy, mx - mix)
#
#area = 0
#for y in range(miy, my + 1):
#  for x in range(mix, mx + 1):
#    if any(ra(a, b, x, y) for a, b in edges):
#      area += 1
#      continue
#    ins = 0
#    for a, b in edges:
#      #if a.imag == b.imag: continue
#      if a.real > x: continue
#      if ra(a, b, a.real, y):
#        ins ^= 1
#
#    area += ins
#
#print(area)
