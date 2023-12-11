with open("i") as f:
  ins, _, *t = f.read().strip().split("\n")

import math
ins = [*map("LR".find, ins)]
mapp = { }
currents = []
for i in t:
  d, l, r = i[:3], i[7:10], i[12:15]
  mapp[d] = (l, r)
  if d[-1] == "A":
    currents.append(d)

steps = 0
was = { }
loops = []
while currents:
  i = ins[steps % len(ins)]
  tor = []
  for j in currents:
    if j[-1] == "Z":
      if j in was:
        loops.append(steps - was[j])
        tor.append(j)
      else:
        was[j] = steps
  c = []
  for cc in currents:
    if cc in tor: continue
    c.append(mapp[cc][i])
  currents = c
  steps += 1

m = 1
for i in loops:
  m = (m * i) // math.gcd(m, i)
print(m)
