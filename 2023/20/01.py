with open("i") as f:
  l = f.read().strip().split("\n")

highs = 0
lows = 0

# name:
#   outputs,
#   type, if '&' inputs, state if '%' else None
#   inputs to process

sig = { }

for i in l:
  a, b = i.split(" -> ")
  n = a[1:]
  o = b.split(", ")

  if a[0] == "&":
    sig[n] = [o, "&", { }]
  elif a[0] == "%":
    sig[n] = [o, "%", False]
  else:
    sig[a] = [o, "", None]

for i in sig:
  o, *_ = sig[i]
  for j in o:
    if j in sig and sig[j][1] == "&":
      sig[j][2][i] = False

def count():
  c = 0
  for i in sorted(n for n in sig if sig[n][1] == "%"):
    c *= 2
    c += sig[i][2]
  #for i in sorted(n for n in sig if sig[n][1] == "&"):
  #  for j in sorted(m for m in sig[i][2]):
  #    c *= 2
  #    c += sig[i][2][j]
  return c

loops = { }
lookup = { }
c = 0
while (co := count()) not in loops:
  loops[co] = [c, highs, lows]
  lookup[c] = co

  print(co)
  #input()

  open = [["button", "broadcaster", False]]
  while open:
    new = []

    for button, name, high in open:
      #print(button, f"-{'high' if high else 'low'}->", name)

      if high: highs += 1
      else: lows += 1

      if name not in sig: continue

      type = sig[name][1]
      if type == "%":
        if high: continue
        ss = not sig[name][2]
        sig[name][2] = ss
      elif type == "&":
        s = sig[name][2]
        s[button] = high
        ss = not all(s[i] for i in s)
      else:
        ss = high

      new.extend([name, i, ss] for i in sig[name][0])

    open = new
  c += 1

pc, preh, prel = loops[co]
loopl = c - pc

print(pc, loopl)
