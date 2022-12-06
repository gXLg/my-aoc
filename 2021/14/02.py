with open("i") as f:
  a, r = f.read().strip().split("\n\n")
  r = { a: b for a,b in [i.split(" -> ") for i in r.split("\n")]}
  c = { }
  p = { }
  for s in r:
    p[s] = 0
    c[s[0]] = 0
    c[s[1]] = 0
  for x in range(len(a) - 1):
    c[a[x]] += 1
    p[a[x:x + 2]] += 1
  c[a[-1]] += 1
  for i in range(40):
    pp = { }
    for pa in p:
      pp[pa] = 0
    for pa in p:
      d = r[pa]
      e = p[pa]
      c[d] += e
      pp[pa[0] + d] += e
      pp[d + pa[1]] += e
    p = pp

  v = c.values()
  print(max(v) - min(v))