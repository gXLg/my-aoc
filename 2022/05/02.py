with open("i") as f:
  st, mo = f.read().split("\n\n")
  mo = mo.strip().split("\n")
  st = st.split("\n")
  x = (len(st) + 1) // 4
  stack = { }
  sl = []
  for i in st[-1].split("   "):
    sl.append(int(i.strip()))
    stack[int(i.strip())] = []
  for j in st[:-1][::-1]:
    for ii in range(0, len(j), 4):
      i = j[ii:ii + 4]
      it = i.strip()[1:-1]
      if not it: continue
      stack[sl[ii // 4]].append(it)

  for i in mo:
    z = i.split(" ")
    a, b, c = map(int, (z[1], z[3], z[5]))
    f = []
    for j in range(a):
      f.append(stack[b].pop())
    for j in f[::-1]:
      stack[c].append(j)

  s = ""
  for i in sl:
    s += stack[i][-1]
  print(s)