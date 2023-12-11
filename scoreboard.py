import sys
import json
import matplotlib.pyplot as plt
import matplotlib.dates as dts
import matplotlib.ticker as tck

with open(sys.argv[1], "r") as file:
  j = json.load(file)

plt.figure(figsize = (15, 30))

days = max(int(d) for id in j["members"] for d in j["members"][id]["completion_day_level"])
data = { id: [0] for id in j["members"] }
offset = 1701406800

for day in range(1, days + 1):

  for part in range(1, 3):
    dd = { }
    for id in j["members"]:
      m = j["members"][id]

      if str(day) in m["completion_day_level"]:
        d = m["completion_day_level"][str(day)]
        if str(part) in d:
          dd[id] = d[str(part)]["get_star_ts"] - offset

    t = sorted([[i, dd[i]] for i in dd], key = lambda a: a[1])
    a = pts = len(j["members"].keys())
    for id, _ in t:
      dd[id] = pts
      pts -= 1
    for id in j["members"]:
      if id in dd:
        data[id].append(data[id][-1] + dd[id])
      else:
        data[id].append(data[id][-1])

  offset += 86_400

for id in data:
  ddd = range(1, days * 2 + 1)
  ddt = [data[id][i] - data[id][i - 1] for i in ddd]

  plt.plot(ddd, ddt, label = id)

hl = zip(*plt.gca().get_legend_handles_labels())

shl = sorted(hl, key = lambda i: data[i[1]][-1], reverse = True)

h = [i[0] for i in shl]
l = [j["members"][i[1]]["name"] or f"anon {i[1]}" for i in shl]

plt.grid()
plt.legend(h, l, ncol = 1, loc = "center left", edgecolor = "w", bbox_to_anchor = (1, 0.5))
plt.savefig("fig.png", bbox_inches = "tight", dpi = 100)
