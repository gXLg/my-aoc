with open("i") as f:

  def add_file(fs, path, file):
    c = fs
    for i in path:
      for j in c:
        if j[0] == i:
          c = j[1]
          break
    c.append(file)

  fs = []
  path = []
  i = 0
  j = f.read().strip().split("\n")
  while i < len(j):
    k = j[i]
    if k[0] == "$":
      cmd = k.split(" ")[1:]
      match cmd[0]:
        case "cd":
          if cmd[1] == "..":
            path.pop()
          elif cmd[1] == "/":
            path = []
          else:
            path.append(cmd[1])
          i += 1
        case "ls":
          i += 1
          while i < len(j) and j[i][0] != "$":
            d = j[i].split(" ")
            if d[0] == "dir":
              add_file(fs, path, [d[1], [], 0])
            else:
              add_file(fs, path, [d[1], int(d[0])])
            i += 1

  smaller = []
  def visit(node, smol = None):
    if len(node) == 2:
      return node[1]
    else:
      sum = 0
      for i in node[1]:
        sum += visit(i, smol)

      if smol is not None:
        if sum >= smol:
          smaller.append(sum)

      return sum

  total = visit(["/", fs, 0])
  free = 70_000_000 - total
  need = 30_000_000 - free
  visit(["/", fs, 0], need)
  print(min(smaller))


