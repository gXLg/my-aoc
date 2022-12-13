with open("i") as f:
  m = f.read().strip().split("\n\n")
  mon = { }
  for i in m:
    a, b, c, d, e, f = i.split("\n")
    a = int(a.split(" ")[-1][:-1])
    b = [*map(int, b.split(":")[1].strip().split(", "))]
    c = c.split("=")[-1].strip()
    d = int(d.split(" ")[-1])
    e = int(e.split(" ")[-1])
    f = int(f.split(" ")[-1])

    mon[a] = [b, c, d, e, f, 0]

for i in range(20):
  for j in mon:
    m = mon[j]
    while m[0]:
      m[5] += 1
      old = m[0].pop(0)
      new = eval(m[1])
      item = new // 3
      if not item % m[2]:
        mon[m[3]][0].append(item)
      else:
        mon[m[4]][0].append(item)

s = [mon[i][5] for i in mon]
m = max(s)
s.remove(m)
print(max(s) * m)