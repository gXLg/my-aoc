with open("t") as f:
  x = [map(int, i) for i in f.read().strip().split("\n")]

  def visit(x, y, fx, fy):
    