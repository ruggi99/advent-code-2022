import re

with open("input.txt") as f:
  data = f.read().splitlines()

for i, line in enumerate(data):
  data[i] = list(map(int, re.match("Sensor at x=(-?[0-9]+), y=(-?[0-9]+): closest beacon is at x=(-?[0-9]+), y=(-?[0-9]+)$", line).group(1, 2, 3, 4)))

max_x = None
min_x = None

for points in data:
  if max_x is None:
    max_x = points[0]
    min_x = points[0]
  if points[0] < min_x:
    min_x = points[0]
  if points[2] < min_x:
    min_x = points[2]
  if max_x < points[0]:
    max_x = points[0]
  if max_x < points[2]:
    max_x = points[2]

max_x += 1500000
min_x -= 100

print(min_x, max_x)

row = ["." for x in range(max_x - min_x)]

row_y = 2_000_000
# row_y = 11

for points in data:
  if points[3] == row_y:
    row[points[2] - min_x] = "B"
  distance = abs(points[0] - points[2]) + abs(points[1] - points[3])
  hor_span = distance - abs(row_y - points[1])
  if hor_span < 0:
    continue
  if min_x > points[0] - hor_span:
    print(min_x, points[0] - hor_span)
    print("Error min")
    exit(1)
  if max_x < points[0] + hor_span + 1:
    print(max_x, points[0] + hor_span)
    print("Error max")
    exit(1)
  for i in range(points[0] - hor_span, points[0] + hor_span + 1):
    if row[i - min_x] == ".":
      row[i - min_x] = "#"

print(row.count("#"))
