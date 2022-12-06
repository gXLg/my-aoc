with open("i") as f:
  x = f.read().strip()
  for i in range(len(x) - 13):
    if len({*x[i:i + 14]}) == 14:
      print(i + 14)
      break
