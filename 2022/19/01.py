
with open("t") as f:
  import re

  i = f.read().strip().split("\n")
  blue = []
  for j in i:
    a = re.findall("\d+", j)
    id, o, c, o1, o2, g1, g2 = map(int, a)
    blue.append((id, o, c, o1, o2, g1, g2))

s = 0

for plan in blue:
  id, po, pc, po1, po2, pg1, pg2 = plan

  diff = (1, 0, 0, 0, 0, 0, 0, 0)
  def make(diff = diff, time = 0):

    print(time, diff[4:])

    if time == 24:
      return diff[-1]

    ffid = []
    ro, rc, rob, rg, o, c, ob, g = diff

    if o >= po:
      ffid.append(make((
        ro + 1, rc, rob, rg,
        o - po + ro, c + rc, ob + rob, g + rg
      ), time + 1))

    if o >= pc:
      ffid.append(make((
        ro, rc + 1, rob, rg,
        o - pc + ro, c + rc, ob + rob, g + rg
      ), time + 1))

    if o >= po1 and c >= po2:
      ffid.append(make((
        ro, rc, rob + 1, rg,
        o - po1 + ro, c - po2 + rc, ob + rob, g + rg
      ), time + 1))

    if o >= pg1 and ob >= pg2:
      ffid.append(make((
        ro, rc, rob, rg + 1,
        o - pg1 + ro, c + rc, ob - pg2 + rob, g + rg
      ), time + 1))

    ffid.append(make((
      ro, rc, rob, rg,
      o + ro, c + rc, ob + rob, g + rg
    ), time + 1))

    return max(ffid)

  m = make() * id
  print(m)
  s += m

print(s)