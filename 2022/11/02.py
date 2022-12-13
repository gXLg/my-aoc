with open("i") as f:
  m = f.read().strip().split("\n\n")
  mon = []
  modulo = 1
  for i in m:
    a, b, c, d, e, f = i.split("\n")
    a = int(a.split(" ")[-1][:-1])
    b = [*map(int, b.split(":")[1].strip().split(", "))]
    c = c.split("=")[-1].strip()

    d = int(d.split(" ")[-1])
    modulo *= d

    e = int(e.split(" ")[-1])
    f = int(f.split(" ")[-1])

    mon.append([b, c, d, e, f, 0])

for i in range(10_000):
  print("r", i)
  for m in mon:
    m[5] += len(m[0])
    for old in m[0]:
      item = eval(m[1]) % modulo
      mon[m[4 - (not item % m[2])]][0].append(item)
    m[0] = []

s = [i[5] for i in mon]
m = max(s)
s.remove(m)
print(max(s) * m)
