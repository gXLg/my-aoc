with open("i") as f:
  ll = f.read().strip().split("\n\n")

def check(a, b):
  for i, j in zip(a, b):
    if type(i) == type(0) and type(j) == type(0):
      if i < j: return True
      elif i > j: return False
    elif type(i) == type([]) and type(j) == type([]):
      r = check(i, j)
      if r == -1:
        continue
      return r
    elif type(i) == type([]) and type(j) == type(0):
      r = check(i, [j])
      if r == -1:
        continue
      return r
    elif type(i) == type(0) and type(j) == type([]):
      r = check([i], j)
      if r == -1:
        continue
      return r

  if len(a) < len(b):
    return True
  elif len(a) > len(b):
    return False
  return -1

glo = [
  [[2]],
  [[6]]
]

for l in ll:
  a, b = map(eval, l.split("\n"))
  glo.append(a)
  glo.append(b)

f = True
while f:
  f = False
  for i in range(len(glo) - 1):
    a, b = glo[i], glo[i + 1]
    if not check(a, b):
      c, d = b, a
      f = True
    else:
      c, d = a, b
    glo[i] = c
    glo[i + 1] = d

s = 1
n = 1
for i in glo:
  if i == [[2]] or i == [[6]]:
    s *= n
  n += 1

print(s)