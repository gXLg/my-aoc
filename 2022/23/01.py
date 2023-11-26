with open("i") as f:
  elves = set()
  for y, i in enumerate(
    f.read().strip().split("\n")
  ):
    for x, j in enumerate(i):
      if j == "#": elves.add(x + y * 1j)

look = [-1j, 1j, -1, 1]

for i in range(10):
  #print(i)
  plan = { }
  plnn = { }
  moved = False
  for e in elves:
    flag = False
    for j in look:
      k = j / 1j + j
      #l = j * 1j + j
      if e + j in elves or e + k in elves:
        flag = True
        break
    if flag:
      for j in look:
        k = j / 1j + j
        l = j * 1j + j
        if (
          e + j not in elves
          and
          e + k not in elves
          and
          e + l not in elves
        ):
          if e + j in plnn:
            plan[e] = None
            if plnn[e + j] is not None:
              plan[plnn[e + j]] = None
              plnn[e + j] = None
          else:
            plan[e] = e + j
            plnn[e + j] = e
          moved = True
          break
  if not moved: break
  #print(elves)
  #print(plan)
  xm = min(elves, key = lambda a: a.real).real
  ym = min(elves, key = lambda a: a.imag).imag
  xM = max(elves, key = lambda a: a.real).real
  yM = max(elves, key = lambda a: a.imag).imag
  f = [
    [
      "." for i in range(int(xm), int(xM) + 1)
    ] for j in range(int(ym), int(yM) + 1)
  ]
  #for i in elves:
  #  j = i - xm - ym * 1j
  #  f[int(j.imag)][int(j.real)] = "#"
  #print(*["".join(i) for i in f], sep = "\n")
  #input()
  new = set()
  for i in elves:
    if i in plan:
      if plan[i] is not None:
        #if plan[i] in new:
          #print("cringe", i)
        new.add(plan[i])
      else:
        #if i in new:
          #print("cringe", i)
        new.add(i)
    else:
      #if i in new:
        #print("cringe", i)
      new.add(i)
  elves = new
  look.append(look.pop(0))

xm = min(elves, key = lambda a: a.real).real
ym = min(elves, key = lambda a: a.imag).imag
xM = max(elves, key = lambda a: a.real).real
yM = max(elves, key = lambda a: a.imag).imag

#print(xm, ym, xM, yM)

print(int(
  (abs(xm - xM) + 1) * (abs(ym - yM) + 1) - len(elves)
))