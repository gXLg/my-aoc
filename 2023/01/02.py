with open("i") as f:
  t = f.read().strip().split("\n")

import re

b = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
d = "(?:" + ")|(?:".join(b) + ")"
s = 0
for i in t:
  a = [*map("".join, re.findall(f"(?=(\\d|{d}))", i))]

  f = str(b.index(a[0]) + 1) if a[0] in b else a[0]
  l = str(b.index(a[-1]) + 1) if a[-1] in b else a[-1]

  s += int(f + l)

print(s)
