with open("i") as f:
  t = f.read().strip().split("\n")

b = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
d = [*"123456789"]
s = 0
for i in t:
  a = []
  for j in range(len(i)):
    for k in b + d:
      if i[j:j + len(k)] == k:
        a.append(k)

  f = a[0]
  l = a[-1]

  if f in b:
    f = str(b.index(f) + 1)

  if l in b:
    l = str(b.index(l) + 1)

  s += int(f + l)

print(s)
