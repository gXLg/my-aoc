with open("i") as f:
  j = [i.strip().split(" ") for i in f.readlines()]
  g = ["A", "B", "C"]
  h = ["X", "Y", "Z"]
  l = 0
  for a, b in j:
    s = h.index(b) * 3
    if s == 6:
      t = ["C", "A", "B"].index(a) + 1
    if s == 3:
      t = g.index(a) + 1
    if s == 0:
      t = ["B", "C", "A"].index(a) + 1
    l += s + t
  print(l)