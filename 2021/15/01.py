with open("t") as f:
  x = [[*map(int, i)] for i in f.read().strip().split("\n")]
  print(x)

  def visit(x, y, fx, fy):
    pass