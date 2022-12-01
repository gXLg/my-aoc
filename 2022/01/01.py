with open("i") as f:
  print(max(sum(map(int, i)) for i in map(str.split, f.read().split("\n\n"))))