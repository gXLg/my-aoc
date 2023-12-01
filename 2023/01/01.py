with open("i") as f:
  t = f.read().split()

import re

s = 0
for i in t:
  a = re.findall("\\d", i)
  s += int(a[0] + a[-1])

print(s)
