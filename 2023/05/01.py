with open("i") as f:
  t = f.read().strip().split("\n")

seeds = [*map(int, t[0].split(": ")[1].split())]

maps = "|".join(t[2:]).split("||")

all = set()

mapp = []
for m in maps:
  _, *c = m.split("|")
  cc = []
  for i in c:
    en, st, r = map(int, i.split())
    mm = (en, st, r)
    cc.append(mm)
  mapp.append(cc)

for seed in seeds:
  for m in mapp:
    for en, st, r in m:
      if seed in range(st, st + r):
        seed = en + seed - st
        break

  all.add(seed)

print(min(all))
