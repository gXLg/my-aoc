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

s = 0
n = 1
for l in ll:
  a, b = map(eval, l.split("\n"))
  c = check(a, b)
  if c:
    s += n

  n += 1

print(s)