with open("i") as f:
  t = f.read().strip().split("\n")

ca = { }
s = 0

for i, card in enumerate(t):
  a, b = card.split(":")
  c, d = b.strip().split("|")

  must = {*map(int, c.split())}
  have = {*map(int, d.split())}

  win = len(must & have)
  mul = ca.get(i, 1)

  for j in range(i + 1, i + win + 1):
    ca[j] = ca.get(j, 1) + mul

  s += ca.get(i, 1)

print(s)
