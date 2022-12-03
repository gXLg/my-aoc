with open("t") as f:
  a, r = f.read().strip().split("\n\n")
  r = { a: b for a,b in [i.split(" -> ") for i in r.split("\n")]}
  l = len(a)
  for i in range(40):
    s = ""
    for x in range(len(a) - 1):
      s += a[x] + r[a[x:x+2]]
    s += a[-1]
    print(i)
    a = s
  c = [a.count(i) for i in {*a}]
  print(max(c) - min(c))
