with open("i") as f:
  t, d = f.read().strip().split("\n")

import math

t = int(t.split(":")[1].replace(" ", ""))
d = int(d.split(":")[1].replace(" ", ""))

a, b = (
  (t + (t * t - 4 * d) ** .5) / 2,
  (t - (t * t - 4 * d) ** .5) / 2
)
if a % 1 == 0: a -= .1
if b % 1 == 0: b += .1
m = math.floor(a) - math.ceil(b) + 1

print(m)
