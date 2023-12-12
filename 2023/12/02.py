with open("i") as f:
  l = f.read().strip().split("\n")

def count(s, cc):
  this = { s: 1 }
  for c, y in enumerate(cc):
    nexts = { }
    for s in this:
      t = f".{s}."
      for i in range(0, len(s) + 1 - y):
        j = s[i:i + y]
        if "#" in s[:i]: break
        if t[i + y + 1] in ".?" and not "." in j:
          r = s[i + y + 1:].strip(".")
          e = ""
          if c < len(cc) - 1:
            while True:
              f = r.find(".")
              if not ~f: break
              if f >= cc[c + 1]: break
              e += r[:f]
              r = r[f:].strip(".")
            if len(r) >= cc[c + 1] and "#" not in e:
              nexts[r] = nexts.get(r, 0) + this[s]
          else:
            nexts[r] = nexts.get(r, 0) + this[s]
    this = nexts

  x = 0
  for i in nexts:
    if "#" not in i:
      x += nexts[i]

  return x

su = 0
for i in l:
  s, b = i.split()
  c = [*map(int, b.split(","))]
  su += count("?".join([s] * 5).strip("."), c * 5)

print(su)
