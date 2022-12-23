from collections import deque

with open("input.txt") as f:
  data = f.read().splitlines()

grid = []

for i in range(10):
  grid.append(["." for x in range(len(data[0]) + 20)])

for line in data:
  grid.append(["." for x in range(10)] + list(line) + ["." for x in range(10)])

for i in range(10):
  grid.append(["." for x in range(len(data[0]) + 20)])

directions = deque(["N", "S", "W", "E"])

def calc_position(y, x, d):
  directions = {"E": (0, 1), "NE": (-1, 1), "N": (-1, 0), "NW": (-1, -1), "W": (0, -1), "SW": (1, -1), "S": (1, 0), "SE": (1, 1)}
  dy, dx = directions[d]
  return y + dy, x + dx

def check_nearby(y, x):
  directions = ["E", "NE", "N", "NW", "W", "SW", "S", "SE"]
  for d in directions:
    _y, _x = calc_position(y, x, d)
    if grid[_y][_x] == "#":
      return True
  return False

def check_can_move(y, x, d):
  if d == "N":
    for i in range(3):
      if grid[y - 1][x - 1 + i] == "#":
        return False
  elif d == "S":
    for i in range(3):
      if grid[y + 1][x - 1 + i] == "#":
        return False
  elif d == "W":
    for i in range(3):
      if grid[y - 1 + i][x - 1] == "#":
        return False
  elif d == "E":
    for i in range(3):
      if grid[y - 1 + i][x + 1] == "#":
        return False
  return True

for i in range(10):
  proposed = []
  grid_copy = [["." for x in range(len(grid[0]))] for y in range(len(grid))]
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      char = grid[y][x]
      if char == ".":
        continue
      if not check_nearby(y, x):
        continue
      for d in directions:
        if not check_can_move(y, x, d):
          continue
        proposed.append(calc_position(y, x, d))
        break
      else:
        pass
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      char = grid[y][x]
      if char == ".":
        continue
      if not check_nearby(y, x):
        grid_copy[y][x] = "#"
        continue
      for d in directions:
        if not check_can_move(y, x, d):
          continue
        proposed_position = calc_position(y, x, d)
        if proposed.count(proposed_position) > 1:
          grid_copy[y][x] = "#"
          break
        grid_copy[proposed_position[0]][proposed_position[1]] = "#"
        break
      else:
        grid_copy[y][x] = "#"
  directions.rotate(-1)
  grid = grid_copy
  del grid_copy

min_x = len(grid[0])
max_x = 0

for line in list(grid):
  if line.count("#") != 0:
    break
  grid.pop(0)

for line in list(reversed(grid)):
  if line.count("#") != 0:
    break
  grid.pop(-1)

for y, line in enumerate(list(grid)):
  line_rev = line[::-1]
  try:
    idx = line.index("#")
    idx_rev = len(line) - line_rev.index("#") - 1
  except:
    continue
  min_x = min(min_x, idx)
  max_x = max(max_x, idx_rev)

count = 0
for line in grid:
  count += line[min_x:max_x + 1].count(".")

print(count)