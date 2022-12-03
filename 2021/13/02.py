with open("i") as f:
  d, f = f.read().split("\n\n")
  s = set()
  for ss in d.split("\n"):
    a, b = map(int, ss.split(","))
    s.add((a, b))
  for ff in f.strip().split("\n"):
    p = ff.split(" ")[-1]
    a, c = p.split("=")
    c = int(c)
    if a == "x":
      s = {(x, y) if x < c else (2 * c - x, y) for x, y in s}
    else:
      s = {(x, y) if y < c else (x, 2 * c - y) for x, y in s}

  # raw output
  for y in range(max(y for x, y in s) + 1):
    l = ""
    for x in range(max(x for x, y in s) + 1):
      l += "#" if (x, y) in s else " "
    print(l)