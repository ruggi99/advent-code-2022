from collections import deque

with open("input.txt") as f:
  data = f.read().splitlines()

height = len(data)
width = len(data[0])

E = 0, 1
S = height - 2, width - 2

class Blizzard:
  __slots__ = ["x", "y", "dir"]
  def __init__(self, y, x, dir) -> None:
    self.y = y
    self.x = x
    self.dir = dir
  
  def __str__(self) -> str:
    return f"y={self.y}, x={self.x}, direction={self.dir}"
  
  def move(self):
    if self.dir == ">":
      if self.x == width - 2:
        self.x = 1
        return
      self.x += 1
      return
    if self.dir == "v":
      if self.y == height - 2:
        self.y = 1
        return
      self.y += 1
      return
    if self.dir == "<":
      if self.x == 1:
        self.x = width - 2
        return
      self.x -= 1
      return
    if self.dir == "^":
      if self.y == 1:
        self.y = height - 2
        return
      self.y -= 1
      return
    

blizzards: deque[Blizzard] = deque()

for y in range(1, height - 1):
  for x in range(1, width - 1):
    if data[y][x] in "<>^v":
      blizzards.append(Blizzard(y, x, data[y][x]))

def get_blizzard_set():
  pos: set[tuple[int, int]] = set()
  for b in blizzards:
    pos.add((b.y, b.x))
  return pos


def run():
  possible_moves = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
  count = 0
  possible_positions = deque([E])
  while True:
    for b in blizzards:
      b.move()
    blizzards_set = get_blizzard_set()
    possible_positions_tmp = deque()
    while possible_positions:
      y, x = possible_positions.pop()
      for dy, dx in possible_moves:
        _y, _x = (y + dy, x + dx)
        new_pos = _y, _x
        if new_pos in blizzards_set:
          continue
        if S == new_pos:
          print(count + 2)
          exit(0)
        if new_pos != E:
          if _y < 1 or _y > height - 2:
            continue
          if _x < 1 or _x > width - 2:
            continue
        possible_positions_tmp.append(new_pos)
    count += 1
    cache = set()
    for p in possible_positions_tmp:
      if p in cache:
        continue
      cache.add(p)
      possible_positions.append(p)

run()
