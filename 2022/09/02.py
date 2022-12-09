with open("i") as f:
  mov = [i.split(" ") for i in f.read().strip().split("\n")]

  d = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
  }

  tailv = { (0, 0) }
  body = [(0, 0) for i in range(10)]

  def touch(head, tail):
    hx, hy = head
    tx, ty = tail
    return ((tx - hx) ** 2 + (ty - hy) ** 2) <= 2

  def delta(head, tail):
    hx, hy = head
    tx, ty = tail
    return ((hx - tx), (hy - ty))

  def move(dir, c):
    tx, ty = c
    dx, dy = dir
    return (tx + dx, ty + dy)

  def abb(dir):
    x, y = dir
    x = 0 if x == 0 else x // abs(x)
    y = 0 if y == 0 else y // abs(y)
    return (x, y)

  for dir, count in mov:
    count = int(count)
    for i in range(count):
      b = [move(d[dir], body[0])]
      for j in range(1, len(body)):
        if not touch(body[j], b[-1]):
          x, y = abb(delta(b[-1], body[j]))
        else:
          x, y = (0, 0)
        b.append(move((x, y), body[j]))
      body = [*b]
      tailv.add(body[-1])

  print(len(tailv))
