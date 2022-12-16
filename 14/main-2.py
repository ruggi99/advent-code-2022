with open("input.txt") as f:
  data = f.read().splitlines()

max_y = 0
max_x = 500
min_x = 500
for i, line in enumerate(data):
  line = line.split(" -> ")
  for t, l in enumerate(line):
    line[t] = list(map(int, l.split(",")))
    if line[t][0] > max_x:
      max_x = line[t][0]
    elif line[t][0] < min_x:
      min_x = line[t][0]
    if line[t][1] > max_y:
      max_y = line[t][1]
  data[i] = line

min_x -= 150
max_x += 150
max_y += 2
print(min_x, max_y, max_x)

cave = [["." for x in range(max_x - min_x + 1)] for y in range(max_y + 1)]
for i in range(max_x - min_x + 1):
  cave[max_y][i] = "#"

def range_plus(start, stop):
  if start <= stop:
    return range(start, stop + 1)
  return range(stop, start + 1)

for points in data:
  curr = points[0]
  for point in points:
    if point == curr:
      continue
    is_vert = (point[0] == curr[0])
    if is_vert:
      for i in range_plus(curr[1], point[1]):
        cave[i][curr[0] - min_x] = "#"
    else:
      for i in range_plus(curr[0], point[0]):
        cave[curr[1]][i - min_x] = "#"
    curr = point

for line in cave:
  print("".join(line))

print()
count = 0
while True:
  x, y = 500 - min_x, 0
  rest = False
  while True:
    if cave[y + 1][x] == ".":
      y += 1
      continue
    if x == 0:
      print("Error")
      exit(1)
    if cave[y + 1][x - 1] == ".":
      y += 1
      x -= 1
      continue
    if cave[y + 1][x + 1] == ".":
      y += 1
      x += 1
      continue
    cave[y][x] = "o"
    count += 1
    if y == 0:
      rest = True
    break
  if rest:
    break

for line in cave:
  print("".join(line))

print(count)