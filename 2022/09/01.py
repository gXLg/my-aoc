with open("i") as f:
  mov = [i.split(" ") for i in f.read().strip().split("\n")]

  d = {
    "R": (-1, 0),
    "L": (1, 0),
    "U": (0, -1),
    "D": (0, 1)
  }

  #cords = set()
  head = (0, 0)
  tail = (0, 0)
  tailv = { tail }

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
      head = move(d[dir], head)
      if not touch(head, tail):
        x, y = abb(delta(head, tail))
        tail = move((x, y), tail)
        tailv.add(tail)
  print(len(tailv))
