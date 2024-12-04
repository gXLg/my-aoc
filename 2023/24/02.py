with open("t") as f:
  p = f.read().strip().split("\n")

#from sympy import divisors as divs

sto = []
for i in p:
  l, r = i.split(" @ ")
  l = [*map(int, l.strip().split(", "))]
  r = [*map(int, r.strip().split(", "))]
  sto.append((l, r))

(ax, ay, az), (avx, avy, avz) = sto[0] # s
(bx, by, bz), (bvx, bvy, bvz) = sto[1] # t
(cx, cy, cz), (cvx, cvy, cvz) = sto[2] # u
#(dx, dy, dz), (dvx, dvy, dvz) = sto[3]

## Equations
#
# _x + _vx * s = x + vx * s
# _y + _vy * s = y + vy * s
# _z + _vz * s = z + vz * s
#

# let x=0 and vx=1 (normalized assumption)
# ax + avx * s = 0 + 1 * s = s
# ax = (1 - avx) * s
s = ax / (1 - avx)
t = bx / (1 - bvx)
u = cx / (1 - cvx)

# ay + avy * s = y + vy * s
# az + avz * s = z + vz * s
#
# by + bvy * t = y + vy * t
# bz + bvz * t = z + vz * t
#
# y = ay + avy*s - vy*s
# by + bvy*t = ay + avy*s - vy*s + vy*t
#            = ay + avy*s + vy*(t - s)
vy = (by - ay + bvy * t - avy * s) / (t - s)
y = ay + avy * s - vy * s

vz = (bz - az + bvz * t - avz * s) / (t - s)
z = az + avz * s - vz * s

x = 0
vx = 1

print(x, y, z)
print(vx, vy, vz)

print("COMPARE")

print(cx + cvx * u, x + vx * u)
print(cy + cvy * u, y + vy * u)
print(cz + cvz * u, z + vz * u)
