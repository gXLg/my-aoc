with open("i") as f:
  t = f.read().strip().split("\n\n")

c = 0
r = 0

for i in t:
  l = i.split("\n")

  for j in range(len(l) - 1):
    flag = True
    for k in range(j + 1):
      m = 2 * j + 1 - k
      if m >= len(l): continue
      if l[m] != l[k]:
        flag = False
        break

    if flag:
      r += j + 1
      break

  for j in range(len(l[0]) - 1):
    flag = True
    for k in range(j + 1):
      m = 2 * j + 1 - k
      if m >= len(l[0]): continue
      if [ii[m] for ii in l] != [ii[k] for ii in l]:
        flag = False
        break

    if flag:
      c += j + 1
      break

print(c + 100 * r)
