with open("i") as f:

  # copy of the day 15/2021

  #from PIL import Image
  import heapq

  zoom = 2

  fi = []
  y = 0
  for i in f.read().strip().split("\n"):
    r = []
    x = 0
    for j in i:
      if j == "S":
        start = (x, y)
        r.append(0)
      elif j == "E":
        finish = (x, y)
        r.append(25)
      else:
        r.append(ord(j) - ord("a"))
      x += 1
    fi.append(r)
    y += 1

  end = (len(fi[0]) - 1, len(fi) - 1)
  ndd = (len(fi[0]) * zoom, len(fi) * zoom)

  #img = Image.new("RGB", ndd)
  #img.paste((255, 255, 255), (0, 0, *ndd))
  #gif = [img]
  #counter = [0]

  def grad_h(h):
    #return (255, 0, 0)
    q = h / get_h(start)
    r = int(255 * q)
    g = int(255 * (1 - q))
    b = 0
    return (r, g, b)

  def grad_g(g):
    return (0, 0, int(255 * (1 - g / 10)))

  def box(node):
    return (
      node[0] * zoom, node[1] * zoom,
      node[0] * zoom + zoom, node[1] * zoom + zoom
    )

  # learned how to do a* algorithm

  open = []
  openn = set()
  closed = set()
  path = { }
  gs = { }

  def astar():
    open_add(start, 0, None)
    while open:
      f, current = heapq.heappop(open)
      #c = min(openn, key = lambda n: gs[n] + get_h(n))
      #openn.remove(c)
      #if c != current:
      #  if gs[c] + get_h(c) != f:
      #    print(c, current, gs[c] + get_h(c), f)
      #    #exit()
      g = gs[current]

      #img = gif[-1].copy()
      #img.paste(grad_g(get_cost(current)), box(current))
      #counter[0] += 1
      #if counter[0] == 100:
      #  gif.append(img)
      #  counter[0] = 0
      #else:
      #  gif[-1] = img

      if current == finish:
        #prec = current
        #while prec is not None:
          #img = gif[-1].copy()
          #img.paste((200, 200, 120), box(prec))
          #gif.append(img)
          #prec = path[prec]

        #return g
        prec = current
        k = -1
        while prec is not None:
          k += 1
          prec = path[prec]
        return k

      closed.add(current)
      expand(current)

  def open_add(node, g, perc):
    #img = gif[-1].copy()
    #img.paste(grad_h(get_h(node)), box(node))
    #counter[0] += 1
    #if counter[0] == 100:
    #  gif.append(img)
    #  counter[0] = 0
    #else:
    #  gif[-1] = img

    f = g + get_h(node)
    #i = -1
    #any(
    #  gs[open[i := n]] + get_h(open[n]) > f
    #  for n in range(len(open))
    #) or (i := -1)
    #if i == -1:
    #  open.append(node)
    #else:
    #  open.insert(i, node)
    #open.add(node)

    heapq.heappush(open, (f, node))
    openn.add(node)

    gs[node] = g
    path[node] = perc



  def get_cost(node):
    return fi[node[1]][node[0]]

  def get_h(node):
    return (
      abs(finish[0] - node[0]) + abs(finish[1] - node[1])
    )

  def expand(node):
    x, y = node
    for dx, dy in [
      [-1, 0], [1, 0],
      [0, -1], [0, 1]
    ]:
      if 0 <= x + dx <= end[0] and 0 <= y + dy <= end[1]:
        cx = x + dx
        cy = y + dy
        new = (cx, cy)
        if get_cost(new) > get_cost(node) + 1:
          continue
        if new in closed:
          continue
        cand_g = gs[node] + 1 #get_cost(new)
        if new in openn:
          if cand_g <= gs[new]:
            gs[new] = cand_g
            path[new] = node
        else:
          open_add(new, cand_g, node)

  print(astar())

  #gif[0].save(
  #  "./vis.gif", save_all = True,
  #  append_images = gif[1:],
  #  optimize = False, duration = 1
  #)