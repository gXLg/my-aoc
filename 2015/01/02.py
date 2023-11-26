with open("i") as f:
  s = f.read()

f = 0
for i, c in enumerate(s):
  if c == ")":
    if f == 0:
      print(i + 1)
      break
    f -= 2
  f += 1
