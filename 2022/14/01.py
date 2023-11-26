with open("i") as f:
  z = f.read().strip().split("\n")

y = []
for i in z:
  y.append([[*map(int, j.split(","))] for j in i.split(" -> ")])

#maxx = 0
maxy = 0
#minx = 9999999
#miny = 9999999
for i in y:
  #mx = max(j[0] for j in i)
  my = max(j[1] for j in i)
  #nx = min(j[0] for j in i)
  #ny = min(j[1] for j in i)

  #if mx > maxx: maxx = mx
  if my > maxy: maxy = my
  #if nx < minx: minx = nx
  #if nx < miny: miny = ny

maxy = maxy + 1

cave = set()
for i in y:
  x, y = i[0]
  cave.add((x, y))
  for xx, yy in i[1:]:
    if xx == x:
      for j in range(min(yy, y), max(yy, y) + 1):
        cave.add((x, j))
    else:
      for j in range(min(xx, x), max(xx, x) + 1):
        cave.add((j, y))
    x, y = xx, yy

sand = set()
s = -1
while True:
  snd = (500, 0)
  s += 1
  finished = False
  while True:
    x, y = snd
    dsnd = x, y + 1
    lsnd = x - 1, y + 1
    rsnd = x + 1, y + 1
    if dsnd not in cave and dsnd not in sand:
      snd = dsnd
    elif lsnd not in cave and lsnd not in sand:
      snd = lsnd
    elif rsnd not in cave and rsnd not in sand:
      snd = rsnd
    else:
      sand.add(snd)
      break
    if snd[1] > maxy:
      finished = True
      break
  if finished: break

print(s)


