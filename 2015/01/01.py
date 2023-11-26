with open("i") as f:
  s = f.read()

print(s.count("(") - s.count(")"))
