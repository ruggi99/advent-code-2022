with open("input.txt") as f:
  data = f.read().splitlines()

for i, line in enumerate(data):
  data[i] = list(map(int, line.split(",")))

max_x = 0
max_y = 0
max_z = 0

for line in data:
  max_x = max(max_x, line[0])
  max_y = max(max_y, line[1])
  max_z = max(max_z, line[2])

max_x += 1
max_y += 1
max_z += 1

print(max_z, max_y, max_x)

grid = [[[False for x in range(max_x)] for y in range(max_y)] for z in range(max_z)]

for line in data:
  grid[line[2]][line[1]][line[0]] = True

sides = 0

for z in range(max_z):
  for y in range(max_y):
    for x in range(max_x):
      if grid[z][y][x] == False:
        continue
      if x == 0:
        sides += 1
      elif grid[z][y][x - 1] == False:
        sides += 1
      if x == (max_x - 1):
        sides += 1
      elif grid[z][y][x + 1] == False:
        sides += 1

      if y == 0:
        sides += 1
      elif grid[z][y - 1][x] == False:
        sides += 1
      if y == (max_y - 1):
        sides += 1
      elif grid[z][y + 1][x] == False:
        sides += 1

      if z == 0:
        sides += 1
      elif grid[z - 1][y][x] == False:
        sides += 1
      if z == (max_z - 1):
        sides += 1
      elif grid[z + 1][y][x] == False:
        sides += 1

print(sides)