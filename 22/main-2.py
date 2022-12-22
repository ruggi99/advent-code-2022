import re
from numpy import interp as _interp

with open("input.txt") as f:
  data = f.read().splitlines()

FACE_SIZE = 50
# FACE_SIZE = 4

path = data[-1]
data = data[:-2]

curr_x = 0
curr_y = 0

for i, ch in enumerate(data[0]):
  if ch != " ":
    curr_x = i
    break

facing = "E"

def interp(x, f_quadrant, rev=False):
  x_quadrant = x // FACE_SIZE
  fp = [FACE_SIZE * f_quadrant, FACE_SIZE * (f_quadrant + 1) - 1]
  if rev:
    fp.reverse()
  return int(_interp(x, [FACE_SIZE * x_quadrant, FACE_SIZE * (x_quadrant + 1) - 1], fp))

def find_wrap_around_example():
  global curr_x, curr_y, facing
  tmp_x, tmp_y = curr_x, curr_y
  tmp_f = facing
  if facing == "E":
    if curr_y < FACE_SIZE:
      tmp_y = interp(curr_y, 2, True)
      tmp_x = FACE_SIZE * 3 + 3
      tmp_f = "W"
    elif curr_y < FACE_SIZE * 2:
      tmp_y = FACE_SIZE * 2
      tmp_x = interp(curr_y, 3, True)
      tmp_f = "S"
    else:
      tmp_y = interp(curr_y, 0, True)
      tmp_x = FACE_SIZE * 2 + 3
      tmp_f = "W"
  if facing == "W":
    if curr_y < FACE_SIZE:
      tmp_y = FACE_SIZE
      tmp_x = interp(curr_y, 0)
      tmp_f = "S"
    elif curr_y < FACE_SIZE * 2:
      tmp_y = FACE_SIZE * 2
      tmp_x = interp(curr_y, 3, True)
      tmp_f = "S"
    else:
      tmp_y = FACE_SIZE * 1 + 3
      tmp_x = interp(curr_y, 1, True)
      tmp_f = "N"
  if facing == "N":
    if curr_x < FACE_SIZE:
      tmp_y = 0
      tmp_x = interp(curr_x, 2, True)
      tmp_f = "S"
    elif curr_x < FACE_SIZE * 2:
      tmp_y = interp(curr_x, 0)
      tmp_x = FACE_SIZE * 2
      tmp_f = "E"
    elif curr_x < FACE_SIZE * 3:
      tmp_y = FACE_SIZE
      tmp_x = interp(curr_x, 0, True)
      tmp_f = "S"
    else:
      tmp_y = interp(curr_x, 1)
      tmp_x = FACE_SIZE * 2 + 3
      tmp_f = "W"
  if facing == "S":
    if curr_x < FACE_SIZE:
      tmp_y = 0
      tmp_x = interp(curr_x, 2, True)
      tmp_f = "N"
    elif curr_x < FACE_SIZE * 2:
      tmp_y = interp(curr_x, 3, True)
      tmp_x = FACE_SIZE * 2 + 3
      tmp_f = "E"
    elif curr_x < FACE_SIZE * 3:
      tmp_y = FACE_SIZE + 3
      tmp_x = interp(curr_x, 0, True)
      tmp_f = "N"
    else:
      tmp_y = interp(curr_x, 1, True)
      tmp_x = 0
      tmp_f = "E"
  char = data[tmp_y][tmp_x]
  assert char != " "
  if char == "#":
    return -1
  curr_y = tmp_y
  curr_x = tmp_x
  facing = tmp_f
  return 0


def find_wrap_around_input():
  global curr_x, curr_y, facing
  tmp_x, tmp_y = curr_x, curr_y
  tmp_f = facing
  if facing == "E":
    if curr_y < FACE_SIZE:
      tmp_y = interp(curr_y, 2, True)
      tmp_x = FACE_SIZE * 2 - 1
      tmp_f = "W"
    elif curr_y < FACE_SIZE * 2:
      tmp_y = FACE_SIZE - 1
      tmp_x = interp(curr_y, 2)
      tmp_f = "N"
    elif curr_y < FACE_SIZE * 3:
      tmp_y = interp(curr_y, 0, True)
      tmp_x = FACE_SIZE * 3 - 1
      tmp_f = "W"
    else:
      tmp_y = FACE_SIZE * 3 - 1
      tmp_x = interp(curr_y, 1)
      tmp_f = "N"
  if facing == "W":
    if curr_y < FACE_SIZE:
      tmp_y = interp(curr_y, 2, True)
      tmp_x = 0
      tmp_f = "E"
    elif curr_y < FACE_SIZE * 2:
      tmp_y = FACE_SIZE * 2
      tmp_x = interp(curr_y, 0)
      tmp_f = "S"
    elif curr_y < FACE_SIZE * 3:
      tmp_y = interp(curr_y, 0, True)
      tmp_x = FACE_SIZE
      tmp_f = "E"
    else:
      tmp_y = 0
      tmp_x = interp(curr_y, 1)
      tmp_f = "S"
  if facing == "N":
    if curr_x < FACE_SIZE:
      tmp_y = interp(curr_x, 1)
      tmp_x = FACE_SIZE
      tmp_f = "E"
    elif curr_x < FACE_SIZE * 2:
      tmp_y = interp(curr_x, 3)
      tmp_x = 0
      tmp_f = "E"
    else:
      tmp_y = FACE_SIZE * 4 - 1
      tmp_x = interp(curr_x, 0)
      tmp_f = "N"
  if facing == "S":
    if curr_x < FACE_SIZE:
      tmp_y = 0
      tmp_x = interp(curr_x, 2)
      tmp_f = "S"
    elif curr_x < FACE_SIZE * 2:
      tmp_y = interp(curr_x, 3)
      tmp_x = FACE_SIZE - 1
      tmp_f = "W"
    else:
      tmp_y = interp(curr_x, 1)
      tmp_x = FACE_SIZE * 2 - 1
      tmp_f = "W"
  char = data[tmp_y][tmp_x]
  assert char != " ", f'{tmp_y}{tmp_x}'
  if char == "#":
    return -1
  curr_y = tmp_y
  curr_x = tmp_x
  facing = tmp_f
  return 0


def move(quantity):
  global curr_x, curr_y
  orig_x, orig_y = curr_x, curr_y
  if facing == "E":
    for i in range(quantity):
      try:
        char = data[curr_y][curr_x + 1]
      except:
        char = " "
      if char == "#":
        return -1
      if char == ".":
        curr_x += 1
    return curr_x - orig_x
  if facing == "W":
    for i in range(quantity):
      if curr_x == 0:
        char = " "
      else:
        char = data[curr_y][curr_x - 1]
      if char == "#":
        return -1
      if char == ".":
        curr_x -= 1
    return orig_x - curr_x
  if facing == "N":
    for i in range(quantity):
      if curr_y == 0:
        char = " "
      else:
        char = data[curr_y - 1][curr_x]
      if char == "#":
        return -1
      if char == ".":
        curr_y -= 1
    return orig_y - curr_y
  if facing == "S":
    for i in range(quantity):
      try:
        char = data[curr_y + 1][curr_x]
      except:
        char = " "
      if char == "#":
        return -1
      if char == ".":
        curr_y += 1
    return curr_y - orig_y

def turn(direction):
  global facing
  cw = {"N": "E", "E": "S", "S": "W", "W": "N"}
  ccw = {"N": "W", "E": "N", "S": "E", "W": "S"}
  if direction == "L":
    facing = ccw[facing]
  else:
    facing = cw[facing]

while path:
  groups = re.match("^(\d+)([A-Z]?)", path).group(1, 2)
  quantity = int(groups[0])
  while True:
    ret = move(quantity)
    # If found a wall or moved to the end
    if ret == -1 or ret == quantity:
      break
    # else I'm on a edge
    quantity -= ret
    ret = find_wrap_around_input()
    # Found a wall on the other side
    if ret == -1:
      break
    quantity -= 1
  if groups[1]:
    turn(groups[1])
  path = path[(len(groups[0]) + len(groups[1])):]

print(curr_y, curr_x)
facing_score = {"E": 0, "S": 1, "W": 2, "N": 3}
print((curr_y + 1) * 1000 + (curr_x + 1) * 4 + facing_score[facing])
