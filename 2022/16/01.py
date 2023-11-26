with open("i") as f:
  cave = f.read().strip().split("\n")

pipes = { }
l = 0
mf = 0
for i in cave:
  a, b = i.split("to valve")
  v = b[1:].strip().split(", ")
  c, d, e, f, g, h, i = a.strip().split(" ")
  name = d
  flow = int(g.split("=")[1][:-1])
  pipes[name] = (0, v + [name + "valve"])
  pipes[name + "valve"] = (flow, v)
  mf += flow
  l += 1
print(l)
print(len(pipes.keys()))
# I will try to implement own algorithm based on A*
#
# I gave up and looked on reddit
# Then I decided to not copy code
#
# I gave up on time efficient solution, just work please!
#
# now my solution is also memory expensive, damnit!
# Can't run on my mobile

class Path:
  def __init__(self, nodes, flow = 0, flown = 0):
    self.nodes = nodes
    self.flow = flow
    self.flown = flown

  def len(self):
    return len(self.nodes) - 1

  def add(self, *nodes):
    for node in nodes:
      if self.len() == 30: break
      self.nodes.append(node)
      self.flown += self.flow
      self.flow += pipes[node][0]

  def copy(self):
    return Path([*self.nodes], self.flow, self.flown)

# rework tree to get shortest way to each next valve
better = { }
for p in pipes:
  better[p] = { }
  paths = [Path([p])]
  while paths:
    path = paths.pop(0)
    for pipe in pipes[path.nodes[-1]][1]:
      if pipe in path.nodes: continue
      if pipe in better[p]: continue
      n = path.copy()
      n.add(pipe)
      if pipe.endswith("valve"):
        if pipes[pipe][0]:
          better[p][pipe] = (n.flown, n.len())
      else:
        paths.append(n)

print("better!")
exit()

ppp = set()
paths = [Path(["AA"])]
while paths:
  p = paths.pop()
  if p.len() == 30:
    ppp.add(p.flown)
  elif p.flow == mf:
    p.add(*["AA" for i in range(30)])
    ppp.add(p.flown)
  else:
    last = p.nodes[-1]
    for i in better[last]:
      if i in p.nodes: continue
      pp = better[last][i]
      n = p.copy()
      n.add(*pp.nodes[1:])
      paths.append(n)

print(max(ppp))
