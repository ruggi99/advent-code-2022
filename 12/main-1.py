with open("input.txt") as f:
  data = f.read().splitlines()

S_pos = [0, 0]
E_pos = [0, 0]

for i, line in enumerate(data):
  try:
    S_index = line.index("S")
    if line:
      S_pos[0] = i
      S_pos[1] = S_index
  except:
    pass
  try:
    E_index = line.index("E")
    if line:
      E_pos[0] = i
      E_pos[1] = E_index
  except:
    pass

class Path:
  def __init__(self, pos, char, count, found = False) -> None:
    self.pos = pos
    self.char = char
    self.count = count
    self.found = found
  def __str__(self) -> str:
    return str(self.__dict__)
  def __repr__(self) -> str:
    return str(self.__dict__)

visited = [[False for x in range(len(data[0]))] for y in range(len(data))]
g_found = False

paths = []
paths.append(Path(S_pos, 'a', 0))
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def run():
  while True:
    for path in list(paths):
      paths.remove(path)
      found = False
      print(path)
      for d in directions:
        y_curr, x_curr = path.pos
        y_dir, x_dir = d
        y = y_curr + y_dir
        x = x_curr + x_dir
        if y < 0 or x < 0:
          continue
        if y >= len(data) or x >= len(data[0]):
          continue
        if visited[y][x]:
          continue
        next_char = data[y][x]
        if next_char == "E":
          if path.char in ["y", "z"]:
            paths.append(Path([y, x], next_char, path.count + 1, True))
            found = True
          continue
        if ord(next_char) > (ord(path.char) + 1):
          continue
        paths.append(Path([y, x], next_char, path.count + 1))
        visited[y][x] = True
      if found:
        return list(filter(lambda x: x.found, paths))

p = run()

print(p)
