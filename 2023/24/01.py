with open("i") as f:
  p = f.read().strip().split("\n")

sto = []
for i in p:
  l, r = i.split(" @ ")
  l = [*map(int, l.strip().split(", "))]
  r = [*map(int, r.strip().split(", "))]
  sto.append((l, r))

#testing = (7, 27)
testing = (200000000000000, 400000000000000)
count = 0

for i, a in enumerate(sto):
  for b in sto[i + 1:]:
    (ax, ay, az), (avx, avy, avz) = a
    (bx, by, bz), (bvx, bvy, bvz) = b

    # part 1 care X, Y
    az = bz = avz = bvz = 0

    absa = (avx ** 2 + avy ** 2 + avz ** 2) ** .5
    absb = (bvx ** 2 + bvy ** 2 + bvz ** 2) ** .5
    if (avx / absa, avy / absa, avz / absa) == (bvx / absb, bvy / absb, bvz / absb):
      #print(a, b, "\nparallel")
      #print()
      continue

    # I)
    # ax + avx * s = bx + bvx * t
    # s = (bx - ax + bvx * t) / avx
    # II)
    # ay + avy * s = by + bvy * t
    # ay + avy * ((bx - ax)/avx + t * bvx/avx) = by + bvy * t
    # ay - by + avy * (bx - ax)/avx = (bvy - avy * bvx/avx) * t
    if bvy == avy * bvx/avx:
      continue
    t = (ay - by + avy * (bx - ax) / avx) / (bvy - avy * bvx/avx)
    s = (bx - ax + bvx * t) / avx
    # Prove
    # III)
    if az + avz * s != bz + bvz * t:
      #print(a, b, "\nnot cross")
      #print()
      continue

    X = ax + avx * s
    Y = ay + avy * s

    f = False
    if s > 0 and t > 0:
      if testing[0] <= X <= testing[1] and testing[0] <= Y <= testing[1]:
        count += 1
        f = True

    #print(a, b)
    #print(X, Y, f, "##", s, t)
    #print()

print(count)

