import random
import math

header, *lines = open("map2.txt").read().split()

R = float(header.split()[2])

H, W = len(lines), len(lines[0])

crops = []

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "x":
            crops.append((x,y))

best_points = {tuple(coord) for coord in crops}

best = 0

for st_x, st_y in crops:
    for j in range(50):
        r = random.random() * R
        a = math.radians(random.random() * 360)
        x = int(st_x + r * math.cos(a))
        y = int(st_y + r * math.sin(a))


        n = sum(1 for X, Y in crops if (x-X)*(x-X) + (y-Y)*(y-Y) <= R*R)

        if n == best:
            best_points.add((x,y))

        elif n > best:
            best = n
            best_points = {(x,y)}

print(best, best_points)