with open("t") as f:
  print(sum(sorted(sum(map(int, i)) for i in map(str.split, f.read().split("\n\n")))[-3:]))