with open("i") as f:
  t = f.read().strip().split("\n")

ranks = { }
bids = { }

li = "J23456789TQKA"

for i in t:
  a, b = i.split()
  b = int(b)

  tc = tuple(map(li.find, a))
  bids[tc] = b

  js = []

  for j in range(5):
    if tc[j] == 0:
      js.append(j)

  pos = set()

  for j in range(13 ** len(js)):
    n = j
    c = [*tc]
    for k in js:
      c[k] = n % 13
      n //= 13

    u = { *c }

    match len(u):
      case 1: r = 6
      case 2: r = 4 + any(c.count(j) == 4 for j in u)
      case 3: r = 2 + any(c.count(j) == 3 for j in u)
      case 4: r = 1
      case _: r = 0

    pos.add(r)
    if r == 6: break

  r = max(pos)
  l = ranks.get(r, [])
  l.append(tc)
  ranks[r] = l

rank = 1
sum = 0

for i in range(7):
  for j in sorted(ranks.get(i, [])):
    sum += rank * bids[j]
    rank += 1

print(sum)
