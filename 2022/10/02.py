with open("i") as f:
  c = f.read().strip().split("\n")

screen = [[" " for i in range(40)] for j in range(6)]

flag = 0
i = 0
X = 1
cycle = 0
while i < len(c):
  if abs((cycle % 40) - X) <= 1:
    screen[cycle % 240 // 40][cycle % 40] = "#"
  cycle += 1
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

print("\n".join("".join(i) for i in screen))