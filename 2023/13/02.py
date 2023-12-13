with open("i") as f:
  t = f.read().strip().split("\n\n")

c = 0
r = 0

for i in t:
  l = i.split("\n")

  for j in range(len(l) - 1):
    flag = 1
    for k in range(j + 1):
      m = 2 * j + 1 - k
      if m >= len(l): continue
      if l[m] != l[k]:
        if sum(l[m][ii] != l[k][ii] for ii in range(len(l[0]))) == 1:
          flag -= 1
        else:
          flag = -1

      if flag < 0:
        break

    if flag == 0:
      r += j + 1
      break

  for j in range(len(l[0]) - 1):
    flag = 1
    for k in range(j + 1):
      m = 2 * j + 1 - k
      if m >= len(l[0]): continue
      ll = [ii[m] for ii in l]
      rr = [ii[k] for ii in l]
      if ll != rr:
        if sum(ll[ii] != rr[ii] for ii in range(len(ll))) == 1:
          flag -= 1
        else:
          flag = -1

      if flag < 0:
        break

    if flag == 0:
      c += j + 1
      break

print(c + 100 * r)
