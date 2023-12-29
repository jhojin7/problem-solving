ax, ay, az = map(int, input().split())
cx, cy, cz = map(int, input().split())
# a 🍰 b = (a.z + b.x, a.y × b.y, a.x + b.z)
bx = cx-az
by = cy//ay
bz = cz-ax
print(bx, by, bz)
