with open("i") as f:
  games = f.read().strip().split("\n")

s = 0
for i, game in enumerate(games):
  l, r = game.split(": ")
  parts = r.split("; ")

  ma = {
    "red": set(),
    "green": set(),
    "blue": set()
  }

  for p in parts:
    c = p.split(", ")
    for col in c:
      num, name = col.split(" ")
      ma[name].add(int(num))

  s += max(ma["green"]) * max(ma["red"]) * max(ma["blue"])

print(s)
