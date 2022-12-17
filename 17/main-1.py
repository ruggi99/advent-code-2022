with open("input.txt") as f:
  data = f.read().removesuffix("\n")

ROCKS = [
  ["####"],
  [".#.", "###", ".#."],
  ["..#", "..#", "###"],
  ["#", "#", "#", "#"],
  ["##", "##"]
]

MAX_ROCKS = 2022


LEN_ROCKS = len(ROCKS)
LEN_JET = len(data)

tall = []

def print_tall():
  for line in tall:
    print("".join(line))

def check_overflow_down(rock, fall_height, left_gap):
  fall_height += 1
  if fall_height <= 0:
    return True
  tall_len = len(tall)
  if tall_len < fall_height:
    return False
  rock_height = len(rock)
  rock_width = len(rock[0])
  rock_copy = []
  for y in range(rock_height):
    rock_copy.append("." * left_gap + rock[y] + "." * (7 - rock_width - left_gap))
  
  start = fall_height - rock_height
  for y in range(max(0, start), fall_height):
    for x in range(7):
      if tall[y][x] == "#" and rock_copy[y - start][x] == "#":
        return False
  return True

def check_overflow_side(rock, fall_height, left_gap, jet):
  rock_width = len(rock[0])
  if jet == "<":
    if left_gap == 0:
      return False
    else:
      left_gap -= 1
  else:
    if 7 - left_gap - rock_width == 0:
      return False
    else:
      left_gap += 1
  rock_height = len(rock)
  rock_copy = []
  for y in range(rock_height):
    rock_copy.append("." * left_gap + rock[y] + "." * (7 - rock_width - left_gap))

  start = fall_height - rock_height
  for y in range(max(0, start), fall_height):
    for x in range(7):
      if tall[y][x] == "#" and rock_copy[y - start][x] == "#":
        return False
  return True

def merge_tall_rock(rock, fall_height, left_gap):
  global tall
  rock_height = len(rock)
  rock_width = len(rock[0])
  rock_copy = []
  assert fall_height >= 0
  for y in range(rock_height):
    rock_copy.append("." * left_gap + rock[y] + "." * (7 - rock_width - left_gap))
  tall = [["." for x in range(7)] for y in range(rock_height - fall_height)] + tall
  offset = max(0, fall_height - rock_height)
  for y in range(rock_height):
    for x in range(7):
      if rock_copy[y][x] == "#":
        tall[y + offset][x] = "#"


def run():
  global tall
  curr_rock = 0
  curr_jet = 0
  for i in range(MAX_ROCKS):
    rock = ROCKS[curr_rock]
    fall_height = -4
    # handle falling and jet movements
    left_gap = 2
    while True:
      mv = check_overflow_down(rock, fall_height, left_gap)
      if not mv:
        break
      fall_height += 1
      jet = data[curr_jet]
      ms = check_overflow_side(rock, fall_height, left_gap, jet)
      if ms:
        if jet == ">":
          left_gap += 1
        else:
          left_gap -= 1
      curr_jet = (curr_jet + 1) % LEN_JET
    merge_tall_rock(rock, fall_height, left_gap)
    curr_rock = (curr_rock + 1) % LEN_ROCKS


run()

print(len(tall))
