with open("i") as f:
  t = f.read().strip().split("\n")
  al = [
    *[chr(i) for i in range(ord("a"), ord("z") + 1)],
    *[chr(i) for i in range(ord("A"), ord("Z") + 1)]
  ]
  s = 0
  for ii in range(0, len(t), 3):
    a, b, c = t[ii:ii + 3]
    any((j := aa) in b and aa in c for aa in a)
    s += al.index(j) + 1
  print(s)