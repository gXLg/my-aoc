with open("i") as f:
  rules, inp = f.read().strip().split("\n\n")

class Machine:
  def __init__(self, i):
    x, m, a, s = [int(j.split("=")[1]) for j in i[1:-1].split(",")]
    self.x = x
    self.m = m
    self.a = a
    self.s = s

  def __radd__(self, a):
    return a + self.x + self.m + self.a + self.s

def prr(cmp):
  return lambda m: eval(f"m.{cmp}")

class Verify:
  def __init__(self, r):
    self.chain = []
    *a, b = r[:-1].split(",")
    for i in a:
      cmp, res = i.split(":")
      self.chain.append([prr(cmp), res])
    self.fall = b

  def __call__(self, machine):
    for pr, res in self.chain:
      if pr(machine):
        return res
    else:
      return self.fall

ru = { }

for i in rules.split("\n"):
  a, b = i.split("{")
  ru[a] = Verify(b)

sum = 0
for i in inp.split("\n"):
  m = Machine(i)
  state = "in"
  while state not in ["A", "R"]:
    state = ru[state](m)
  if state == "A":
    sum += m

print(sum)
