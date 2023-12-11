with open("i") as f:
  m = f.read().strip().split("\n")

p = "".join(m).find("S")
W = len(m[0])
H = len(m)

start = current = complex(p % W, p // W)
tile = "S"
pipe = set()

ss = []

dirx = {
  1: "-7J",
  -1j: "|7F",
  -1: "-FL",
  1j: "|LJ"
}
dd = { 1, -1, 1j, -1j }

ex = {
  "-": { 1, -1 },
  "|": { 1j, -1j },
  "7": { -1, 1j },
  "L": { -1j, 1 },
  "J": { -1, -1j },
  "F": { 1, 1j },
  "S": dd
}

f = 0

while True:
  for d in dd & ex[tile]:
    r = current + d

    if (
      (r.imag in range(H) and r.real in range(W))
      and
      (r not in pipe)
      and
      ((tile := m[int(r.imag)][int(r.real)]) in dirx[d])
    ):
      pipe.add(current)
      current = r
      if len(ss) == 0:
        ss.append(dirx[-d])
      break

  else:
    pipe.add(current)
    ss.append(dirx[start - current])
    break

st = [*({ *ss[0] } & { *ss[1] })][0]

area = { }
inside = 0

for y in range(H):
  for x in range(W):
    c = complex(x, y)
    if c in pipe: continue
    for d in dd:
      r = c + d
      if r in area:
        area[c] = area[r]
        inside += area[r]
        break
    else:
      i = 0
      cc = c - 1 - 1j
      while cc.imag >= 0 and cc.real >= 0:
        tile = m[int(cc.imag)][int(cc.real)]
        if cc == start:
          tile = st
          #print("cross start")
        if cc in pipe and tile in "-|JF":
          i ^= 1
        cc -= 1 + 1j

      area[c] = i
      inside += i

print(inside)
