with open("i") as f:
  L = f.read().strip().split("\n")

sum = 0
for i in L:
  num = [*map(int, i.split())]

  layers = [num]
  current = num
  while any(current):
    l = []
    for j in range(len(current) - 1):
      l.append(current[j + 1] - current[j])
    layers.append(l)
    current = l

  add = 0
  for j in layers[::-1]:
    add = j[0] - add

  sum += add

print(sum)
