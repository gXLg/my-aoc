with open("i") as f:
  t = f.read().strip().split("\n")

s = 0
for i in t:
  a, b = i.split(":")
  c, d = b.strip().split("|")

  must = {*map(int, c.split())}
  have = {*map(int, d.split())}

  s += 2 ** len(must & have) // 2

print(s)
