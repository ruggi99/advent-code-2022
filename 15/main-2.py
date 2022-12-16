import re

with open("input.txt") as f:
  data = f.read().splitlines()

# max_grid = 20
max_grid = 4_000_000

for i, line in enumerate(data):
  points = list(map(int, re.match("Sensor at x=(-?[0-9]+), y=(-?[0-9]+): closest beacon is at x=(-?[0-9]+), y=(-?[0-9]+)$", line).group(1, 2, 3, 4)))
  points.append(abs(points[0] - points[2]) + abs(points[1] - points[3]))
  data[i] = points

def check_intersect(y, x):
  for point in data:
    distance = point[4]
    hor_span = distance - abs(y - point[1])
    if (point[0] - hor_span) <= x < (point[0] + hor_span + 1):
      return True
  return False


def run():
  for point in data:
    distance = point[4] + 1
    for side in ["N", "S"]:
      for x in range(max(0, point[0] - distance), min(max_grid, point[0] + distance + 1)):
        vert_span = distance - abs(x - point[0])
        if side == "N":
          y = point[1] - vert_span
          if y < 0 or y > max_grid:
            continue
        else:
          y = point[1] + vert_span
          if y < 0 or y > max_grid:
            continue
        if not check_intersect(y, x):
          return y, x
  return 0, 0


y, x = run()

print(y, x, x * 4_000_000 + y)