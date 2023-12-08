with open("i") as f:
  t = f.read().strip().split("\n")

ranks = { }
bids = { }

li = "23456789TJQKA"

for i in t:
  a, b = i.split()
  b = int(b)

  c = tuple(map(li.find, a))
  bids[c] = b

  u = { *c }

  match len(u):
    case 1: r = 6
    case 2: r = 4 + any(c.count(j) == 4 for j in u)
    case 3: r = 2 + any(c.count(j) == 3 for j in u)
    case 4: r = 1
    case _: r = 0

  l = ranks.get(r, [])
  l.append(c)
  ranks[r] = l

rank = 1
sum = 0

for i in range(7):
  for j in sorted(ranks.get(i, [])):
    sum += rank * bids[j]
    rank += 1

print(sum)
