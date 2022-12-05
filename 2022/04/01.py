with open("i") as f:
  i = 0
  for j in f.read().strip().split("\n"):
    l, r = j.split(",")
    a, b = map(int, l.split("-"))
    c, d = map(int, r.split("-"))
    if (a <= c and b >= d) or (a >= c and b <= d):
      i += 1
  print(i)