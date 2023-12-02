with open("i") as f:
  games = f.read().strip().split("\n")

R = 12
G = 13
B = 14

maxx = {
  "red": 12,
  "green": 13,
  "blue": 14
}

s = 0
for i, game in enumerate(games):
  l, r = game.split(": ")
  parts = r.split("; ")
  flag = True
  for p in parts:
    c = p.split(", ")
    for col in c:
      num, name = col.split(" ")
      if int(num) > maxx[name]:
        flag = False
        break
    if not flag: break
  if flag:
    s += i + 1

print(s)
