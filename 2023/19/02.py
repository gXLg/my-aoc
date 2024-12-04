with open("i") as f:
  rules, inp = f.read().strip().split("\n\n")

class Range:
  def __init__(self, x = 1, xx = 4001, m = 1, mm = 4001, a = 1, aa = 4001, s = 1, ss = 4001):
    self.x = (x, xx)
    self.m = (m, mm)
    self.a = (a, aa)
    self.s = (s, ss)

  def rem(self, string):
    let, op = string[:2]
    num = int(string[2:])
    a, aa = getattr(self, let)
    if op == ">": aa = min(num + 1, aa)
    else: a = max(num, a)
    if a > aa: aa = a = 0
    setattr(self, let, (a, aa))

  def __and__(self, r):
    return Range(
      *Range.andHelper(self.x, r.x),
      *Range.andHelper(self.m, r.m),
      *Range.andHelper(self.a, r.a),
      *Range.andHelper(self.s, r.s)
    )

  def pos(self):
    x, xx = self.x
    m, mm = self.m
    a, aa = self.a
    s, ss = self.s
    return (xx - x) * (mm - m) * (aa - a) * (ss - s)

  @classmethod
  def toRange(clazz, string):
    let, op = string[:2]
    num = int(string[2:])
    if op == ">": num += 1
    else: let *= 2

    a = { let: num }
    return Range(**a)

  @classmethod
  def andHelper(clazz, x, y):
    a, aa = x
    b, bb = y
    xx = max(a, b)
    yy = min(aa, bb)
    if xx > yy:
      yy = xx = 0
    return (xx, yy)

class Verify:
  def __init__(self, r):
    self.checks = []
    *a, b = r[:-1].split(",")
    ran = Range()
    for i in a:
      l, res = i.split(":")
      r = ran & Range.toRange(l)
      self.checks.append((res, r))
      ran.rem(l)
    self.checks.append((b, ran))

ru = { }
for i in rules.split("\n"):
  a, b = i.split("{")
  ru[a] = Verify(b)

open = []
for i in ru:
  r = ru[i]
  for name, check in r.checks:
    if name == "A":
      open.append([i, check])

final = []

while open:
  oo = []
  for i, rc in open:
    for j in ru:
      r = ru[j]
      for name, check in r.checks:
        if name == i:
          s = rc & check
          if j == "in":
            final.append(s)
          else:
            oo.append([j, s])
  open = oo

s = 0
for i in final:
  s += i.pos()

print(s)
