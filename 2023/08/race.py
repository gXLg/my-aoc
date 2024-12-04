def xgcd(a, b):
  tr, r = a, b
  ts, s = 1, 0
  tt, t = 0, 1

  while r:
    q = tr // r
    tr, r = r, tr - q * r
    ts, s = s, ts - q * s
    tt, t = t, tt - q * t
  return tr, ts, tt

def lcm(a, b):
  return a * b // xgcd(a, b)[0]

def axcmod(a, c, d):
  r = xgcd(xgcd(a, c)[0], d)[0]
  a //= r
  c //= r
  d //= r
  _, s, t = xgcd(a, d)
  x = (s * c) % d
  #assert (a * x) % d == c
  return x, d

def race(pre1, cyc1, pre2, cyc2):
  x, d = axcmod(cyc1, pre2 - pre1, cyc2)
  print(x, d)
  while True:
    y = (pre1 - pre2 + cyc1 * x) // cyc2
    if x > 0 and y > 0:
      break
    x += d
  assert pre1 + cyc1 * x == pre2 + cyc2 * y
  return x, y

def ghosts(pairs):
  p, c = pairs.pop(0)
  while pairs:
    p2, c2 = pairs.pop(0)

    x, y = race(p, c, p2, c2)
    p = p + c * x
    c = lcm(c, c2)

  return p

print(race(2, 3, 7, 5))

#print(ghosts([
#  [2, 3],
#  [7, 5],
#  [13, 7]
#]))
