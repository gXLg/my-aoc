with open("i") as f:
  m = f.read().strip().split("\n")

p = "".join(m).find("S")
W = len(m[0])
H = len(m)

current = complex(p % W, p // W)
tile = "S"
pipe = set()

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
      break

  else:
    pipe.add(current)
    break

print(len(pipe) // 2)
