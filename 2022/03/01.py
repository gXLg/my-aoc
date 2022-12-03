with open("i") as f:
  t = f.read().strip().split("\n")
  al = [
    *[chr(i) for i in range(ord("a"), ord("z") + 1)],
    *[chr(i) for i in range(ord("A"), ord("Z") + 1)]
  ]
  s = 0
  for i in t:
    a, b = i[:len(i) // 2], i[len(i) // 2:]
    any((j := bb) in a for bb in b)
    s += al.index(j) + 1
  print(s)