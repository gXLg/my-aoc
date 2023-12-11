with open("i") as f:
  ins, _, *t = f.read().strip().split("\n")

ins = [*map("LR".find, ins)]

mapp = { }

for i in t:
  d, l, r = i[:3], i[7:10], i[12:15]
  mapp[d] = (l, r)

steps = 0
current = "AAA"
was = { }
while current != "ZZZ":
  i = ins[steps % len(ins)]


  was[(current, i)] = steps
  current = mapp[current][i]
  steps += 1

print(steps)
