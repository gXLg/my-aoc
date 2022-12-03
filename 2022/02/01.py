with open("i") as f:
  j = [i.strip().split(" ") for i in f.readlines()]
  g = ["A", "B", "C"]
  h = ["X", "Y", "Z"]
  l = 0
  for a, b in j:
    match a + b:
      case "AX":
        s = 3
      case "AY":
        s = 6
      case "AZ":
        s = 0
      case "BX":
        s = 0
      case "BY":
        s = 3
      case "BZ":
        s = 6
      case "CX":
        s = 6
      case "CY":
        s = 0
      case "CZ":
        s = 3
    l += s + h.index(b) + 1
  print(l)