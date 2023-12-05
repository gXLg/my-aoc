with open("i") as f:
  t = f.read().strip().split("\n")

r = [*map(int, t[0].split(": ")[1].split())]
seeds = [*zip(r[::2], r[1::2])]
maps = "|".join(t[2:]).split("||")
mapp = []
for m in maps:
  _, *c = m.split("|")
  mapp.append([[*map(int, i.split())] for i in c])

all = set()
for begin, length in seeds:
  ranges = { (begin, begin + length) }
  for m in mapp:
    translated = set()
    for end, start, leng in m:
      diff = end - start
      temp = set()
      for a, b in ranges:
        if a < start <= b:
          temp.add((a, start))
          a = start
        if a < b and start <= a < start + leng:
          x = a
          if b < start + leng: y = a = b
          else: y = a = start + leng
          translated.add((x + diff, y + diff))
        if a < b:
          temp.add((a, b))

      ranges = temp
    ranges |= translated

  all.add(min(a for a, b in ranges))

print(min(all))
