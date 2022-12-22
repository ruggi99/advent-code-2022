import re

with open("input.txt") as f:
  data = f.read().splitlines()

path = data[-1]
data = data[:-2]

curr_x = 0
curr_y = 0

for i, ch in enumerate(data[0]):
  if ch != " ":
    curr_x = i
    break


facing = "E"

def find_wrap_around():
  if facing == "E":
    tmp_x = curr_x - 1
    while True:
      if tmp_x == 0 or data[curr_y][tmp_x - 1] == " ":
        if data[curr_y][tmp_x] == "#":
          return curr_x
        return tmp_x
      tmp_x -= 1
  if facing == "W":
    tmp_x = curr_x + 1
    while True:
      try:
        char = data[curr_y][tmp_x + 1]
      except:
        char = " "
      if char == " ":
        if data[curr_y][tmp_x] == "#":
          return curr_x
        return tmp_x
      tmp_x += 1
  if facing == "N":
    tmp_y = curr_y + 1
    while True:
      try:
        char = data[tmp_y + 1][curr_x]
      except:
        char = " "
      if char == " ":
        if data[tmp_y][curr_x] == "#":
          return curr_y
        return tmp_y
      tmp_y += 1
  if facing == "S":
    tmp_y = curr_y - 1
    while True:
      if tmp_y == 0 or data[tmp_y - 1][curr_x] == " ":
        if data[tmp_y][curr_x] == "#":
          return curr_y
        return tmp_y
      tmp_y -= 1


def move(quantity):
  global curr_x, curr_y
  quantity = int(quantity)
  if facing == "E":
    for i in range(quantity):
      try:
        char = data[curr_y][curr_x + 1]
      except:
        char = " "
      if char == "#":
        break
      if char == ".":
        curr_x += 1
        continue
      curr_x = find_wrap_around()
    return
  if facing == "W":
    for i in range(quantity):
      if curr_x == 0:
        char = " "
      else:
        char = data[curr_y][curr_x - 1]
      if char == "#":
        break
      if char == ".":
        curr_x -= 1
        continue
      curr_x = find_wrap_around()
    return
  if facing == "N":
    for i in range(quantity):
      if curr_y == 0:
        char = " "
      else:
        char = data[curr_y - 1][curr_x]
      if char == "#":
        break
      if char == ".":
        curr_y -= 1
        continue
      curr_y = find_wrap_around()
    return
  if facing == "S":
    for i in range(quantity):
      try:
        char = data[curr_y + 1][curr_x]
      except:
        char = " "
      if char == "#":
        break
      if char == ".":
        curr_y += 1
        continue
      curr_y = find_wrap_around()
    return

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

  move(groups[0])
  if groups[1]:
    turn(groups[1])
  path = path[(len(groups[0]) + len(groups[1])):]

print(curr_y, curr_x)
facing_score = {"E": 0, "S": 1, "W": 2, "N": 3}
print((curr_y + 1) * 1000 + (curr_x + 1) * 4 + facing_score[facing])
