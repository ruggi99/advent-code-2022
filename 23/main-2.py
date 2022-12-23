from collections import deque

with open("input.txt") as f:
  data = f.read().splitlines()

CYCLES = 1000

grid = []

for i in range(CYCLES // 2):
  grid.append(["." for x in range(len(data[0]) + CYCLES)])

for line in data:
  grid.append(["." for x in range(CYCLES // 2)] + list(line) + ["." for x in range(CYCLES // 2)])

for i in range(CYCLES // 2):
  grid.append(["." for x in range(len(data[0]) + CYCLES)])

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

for i in range(CYCLES):
  proposed = []
  grid_copy = [["." for x in range(len(grid[0]))] for y in range(len(grid))]
  moved = False
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
        moved = True
        break
      else:
        grid_copy[y][x] = "#"
  if moved == False:
    print(i + 1)
    exit(0)
  directions.rotate(-1)
  grid = grid_copy
  del grid_copy