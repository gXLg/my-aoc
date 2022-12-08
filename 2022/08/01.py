with open("i") as f:
  forest = [[int(j) for j in i] for i in f.read().strip().split("\n")]

  count = len(forest[0]) * 2 + len(forest) * 2 - 4

  for y in range(1, len(forest) - 1):
    for x in range(1, len(forest[0]) - 1):
      tree = forest[y][x]

      row = forest[y]
      column = [i[x] for i in forest]

      a = row[x:]
      b = row[:x + 1]
      c = column[y:]
      d = column[:y + 1]

      #print(a, b, c, d, sep = "\n")

      if any(
        i.count(tree) == 1 and max(i) == tree
        for i in [a, b, c, d]
      ): count += 1

  print(count)