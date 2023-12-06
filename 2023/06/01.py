with open("i") as f:
  t, d = f.read().strip().split("\n")

import math

t = map(int, t.split(":")[1].strip().split())
d = map(int, d.split(":")[1].strip().split())

m = 1
for tt, dd in zip(t, d):
  a, b = (
    (tt + (tt * tt - 4 * dd) ** .5) / 2,
    (tt - (tt * tt - 4 * dd) ** .5) / 2
  )
  if a % 1 == 0: a -= .1
  if b % 1 == 0: b += .1
  m *= math.floor(a) - math.ceil(b) + 1

print(m)
