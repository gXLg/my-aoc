with open("i") as f:
  c = f.read().strip().split("\n")

flag = 0
i = 0
X = 1
cycle = 0
s = 0
while i < len(c):
  cycle += 1
  if not (cycle - 20) % 40:
    s += cycle * X
  m = c[i]
  if m == "noop":
    i += 1
    continue
  a, b = m.split(" ")
  b = int(b)
  if flag:
    i += 1
    X += b
    flag = 0
    continue
  flag = 1

print(s)