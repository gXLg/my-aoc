with open("i") as f:
  mon = { a[:4]: a[6:] for a in f.read().strip().split("\n") }


lr = []
def visit(m = "root"):
  if m == "humn":
    return "uga buga"

  a = mon[m].split(" ")
  if len(a) != 1:
    l, op, r = a
    ll, rr = visit(l), visit(r)
    if ll == "uga buga":
      lr.append(1)
    elif rr == "uga buga":
      lr.append(0)
    else:
      return
    return "uga buga"

def solve(m, uga = None):

  a = mon[m].split(" ")

  if uga is not None:
    if m == "humn":
      return uga

    l, op, r = a
    p = lr.pop()
    if p == 0:
      if op == "+":
        return solve(r, uga - solve(l))
      if op == "-":
        return solve(r, solve(l) - uga)
      if op == "*":
        return solve(r, uga // solve(l))
      if op == "/":
        return solve(r, solve(l) // uga)
    else:
      if op == "+":
        return solve(l, uga - solve(r))
      if op == "-":
        return solve(l, solve(r) + uga)
      if op == "*":
        return solve(l, uga // solve(r))
      if op == "/":
        return solve(l, solve(r) * uga)

  else:
    if len(a) == 1:
      return int(a[0])
    else:
      l, op, r = a
      op = op.replace("/", "//")
      return eval(f"{solve(l)} {op} {solve(r)}")


visit()

l, op, r = mon["root"].split(" ")
p = lr.pop()
if p == 0:
  s = solve(r, solve(l))
else:
  s = solve(l, solve(r))

print(s)