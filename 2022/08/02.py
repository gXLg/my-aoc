with open("i") as f:
  forest = [[int(j) for j in i] for i in f.read().strip().split("\n")]

  counts = []

  for y in range(1, len(forest) - 1):
    for x in range(1, len(forest[0]) - 1):
      tree = forest[y][x]

      row = forest[y]
      column = [i[x] for i in forest]

      a = row[x:]
      b = row[:x + 1][::-1]
      c = column[y:]
      d = column[:y + 1][::-1]

      s = 1
      for i in [a, b, c, d]:
        k = 0
        for j in i[1:]:
          k += 1
          if j >= tree:
            break
        s *= k
      counts.append(s)


  print(max(counts))