with open("input.txt") as f:
  data = f.read().splitlines()

dim = 500
x_start = 35
y_start = 200
tail_visited = [[False for x in range(dim)] for y in range(dim)]
tail_visited[y_start][x_start] = True

# 1 head + 9 tails
pos = [[y_start, x_start] for y in range(10)]

for line in data:
  dire, quant = line.split(" ")
  quant = int(quant)
  for i in range(quant):
    if dire == "U":
      pos[0][0] -= 1
    elif dire == "D":
      pos[0][0] += 1
    elif dire == "L":
      pos[0][1] -= 1
    else:
      pos[0][1] += 1
    if pos[0][0] < 0 or pos[0][0] >= dim:
      print("Error", pos[0])
      exit(1)
    if pos[0][1] < 0 or pos[0][1] >= dim:
      print("Error", pos[0])
      exit(1)
    for t in range(1, 10):
      vert = pos[t - 1][0] - pos[t][0]
      hori = pos[t - 1][1] - pos[t][1]
      need_update = abs(vert) >= 2 or abs(hori) >= 2
      # print(need_update)
      if need_update:
        # Same row or column
        if vert > 0:
          pos[t][0] += 1
        elif vert < 0:
          pos[t][0] -= 1
        if hori > 0:
          pos[t][1] += 1
        elif hori < 0:
          pos[t][1] -= 1
    tail_visited[pos[9][0]][pos[9][1]] = True
  print(pos)

n_true = 0
for line in tail_visited:
  n_true += sum(line)

print(n_true)