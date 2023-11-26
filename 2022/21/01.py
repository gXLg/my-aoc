with open("i") as f:
  mon = { a[:4]: a[6:] for a in f.read().strip().split("\n") }

def visit(m = "root"):
  a = mon[m].split(" ")
  if len(a) == 1:
    return int(a[0])
  else:
    l, op, r = a
    op = op.replace("/", "//")
    return eval(f"{visit(l)} {op} {visit(r)}")

print(visit())