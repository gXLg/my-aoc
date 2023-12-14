with open("i") as f:
  t = f.read().strip().split("\n")

steady = set()
loose = []

for y, l in enumerate(t):
  for x, stone in enumerate(l):
    cords = complex(x, y)
    if stone == "#": steady.add(cords)
    elif stone == "O": loose.append(cords)

sum = 0
for stone in loose:
  while stone.imag > 0 and not stone - 1j in steady:
    stone -= 1j

  steady.add(stone)

  sum += len(t) - stone.imag

print(int(sum))
