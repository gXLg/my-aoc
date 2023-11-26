with open("i") as f:
  push = f.read().strip()

rocks = [
  {(0, 0), (1, 0), (2, 0), (3, 0)},
  {(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)},
  {(2, 2), (2, 1), (0, 0), (1, 0), (2, 0)},
  {(0, 0), (0, 1), (0, 2), (0, 3)},
  {(0, 0), (1, 0), (0, 1), (1, 1)}
]

cave = set()
def pupu(ro, pp):
  #print("moving rock", r, "to", pp)
  if pp == ">":
    roro = {(x + 1, y) for x, y in ro}
    if any(x > 6 or (x, y) in cave for x, y in roro):
      #print("aborted")
      return ro
    return roro
  elif pp == "<":
    roro = {(x - 1, y) for x, y in ro}
    if any(x < 0 or (x, y) in cave for x, y in roro):
      #print("aborted")
      return ro
    return roro
  elif pp == "v":
    roro = {(x, y - 1) for x, y in ro}
    if any((x, y) in cave or y < 0 for x, y in roro):
      #print("aborted, stay")
      return ro
    return roro

r = -1
p = -1
top = -1

for i in range(2022):

  r = (r + 1) % len(rocks)

  rock = rocks[r]
  rock = {(x + 2, y + top + 4) for x, y in rock}

  #print("cycle", i)

  while True:

    p = (p + 1) % len(push)
    pp = push[p]

    #for j in range(top + 5, -1, -1):
    #  print("|" + "".join(".#@"[((x, j) in cave) - ((x, j) in rock)] for x in range(7)) + "|")
    #print("+" + "-" * 7 + "+")
    #print(pp)
    #input()

    rock = pupu(rock, pp)
    ro = pupu(rock, "v")
    if rock == ro:
      cave.update(rock)
      my = 0
      for x, y in cave:
        if y > my: my = y
      top = my
      break
    else:
      rock = ro

print(top + 1)

