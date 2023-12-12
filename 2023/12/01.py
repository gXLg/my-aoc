with open("i") as f:
  l = f.read().strip().split("\n")

su = 0

def count(s, c):
  if not c:
    return not "#" in s
  x = 0
  y, *z = c
  t = f".{s}."
  for i in range(0, len(s) + 1 - y):
    j = s[i:i + y]
    if t[i + y + 1] in ".?" and not "." in j and not "#" in t[:i + 1]:
      r = s[i + y + 1:]
      x += count(r, z)

  return x

for i in l:
  s, b = i.split()
  c = [*map(int, b.split(","))]
  su += count(s, c)

print(su)
