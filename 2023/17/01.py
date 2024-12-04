with open("t") as f:
  l = f.read().strip().split("\n")

end = complex(len(l[0]) - 1, len(l) - 1)

def heu(point):
  a = end - point
  return int(a.imag ** 2 + a.real ** 2)

# was, last, weight, direction, heuristic
paths = { ((0 + 0j, ), 0 + 0j, 0, 0, heu(0 + 0j)) }
lasts = set()

while paths:
  p = min(paths, key = lambda a: a[4])
  paths.discard(p)
  was, last, weight, dir, h = p
  #print(weight, last)

  for delt in [1, -1, 1j, -1j]:
    if delt in [dir, -dir]: continue

    cord = last
    w = { *was }
    we = weight

    for _ in range(3):
      cord += delt
      if not cord.real in range(len(l[0])) or not cord.imag in range(len(l)):
        break
      if cord in w: break

      d = int(l[int(cord.imag)][int(cord.real)])
      we += d
      h = we + heu(cord)

      if cord == end:
        lasts.add(we)
        print(we)
      else:
        if not any((cord, we, delt) == (a, b, c) for _, a, b, c, _ in paths):
          w.add(cord)
          paths.add((tuple(w), cord, we, delt, h))

print(min(last))

#start = 0 + 0j
#open = { start }
#gScore = { start: 0 }
#fScore = { start: heu(start) }
#cameFrom = { }
#dirs = { start: 0 }
#
#while open:
#  cordc = sorted(open, key = lambda a: fScore[a])[0]
#  open.discard(cordc)
#  dir = dirs[cordc]
#
#  # TODO: instead of counting same
#  # which can break when re-branching,
#  # add three end-points to openSet in the same direction,
#  # and neber rebranch into one of the same direction
#
#  for delt in [1, -1, 1j, -1j]:
#
#    cord = cordc
#    if delt in [dir, -dir]: continue
#
#    for lenn in range(3):
#
#      nei = cord + delt
#
#      if not nei.real in range(len(l[0])) or not nei.imag in range(len(l)):
#        break
#
#      d = int(l[int(nei.imag)][int(nei.real)])
#
#      tent_g = gScore[cord] + d
#
#      if nei not in gScore or tent_g < gScore[nei]:
#        dirs[nei] = delt
#        cameFrom[nei] = cord
#        gScore[nei] = tent_g
#        fScore[nei] = tent_g + heu(nei)
#        open.add(nei)
#
#      cord = nei
#
#
#print(gScore[end])
#
#current = end
#while current != start:
#  current = cameFrom[current]
#  print(current ) #, dirs[current])
