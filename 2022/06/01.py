with open("i") as f:
  x = f.read().strip()
  for i in range(len(x) - 3):
    if len({*x[i:i + 4]}) == 4:
      print(i + 4)
      break
