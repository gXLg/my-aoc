with open("i") as f:
  enc = [*map(int, f.read().strip().split("\n"))]

# enc = [1, 100, 2, 3]

# 5000
l = len(enc)

#print(enc)
was = set()
order = [i for i in enc]
for mix in order:

  #mix = 100

  if mix in was: continue
  was.add(mix)
  if mix == 0: continue

  idx = []
  [a == mix and idx.append(i) for i, a in enumerate(enc)]
  li = len(idx)
  for ii in range(li):
    i = idx[ii]
    enc.pop(i)
    ni = (i + mix) % (l - 1)
    enc.insert(ni, mix)
    for jj in range(li):
      if ni <= idx[jj] < i:
        idx[jj] += 1
      if i < idx[jj] <= ni:
        idx[jj] -= 1

  #print(mix)
  #print(*[str(i) + (i == mix and "<<" or "") for i in enc])
  #input()

i = enc.index(0)
a = enc[(i + 1000) % l]
b = enc[(i + 2000) % l]
c = enc[(i + 3000) % l]
print(a, b, c)
print("result:", a + b  + c)
