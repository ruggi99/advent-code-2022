with open("input.txt") as f:
  data = f.read().splitlines()

dim = 500
x_start = 35
y_start = 200
tail_visited = [[False for x in range(dim)] for y in range(dim)]
tail_visited[y_start][x_start] = True

H_pos = [y_start, x_start]
T_pos = [y_start, x_start]

for line in data:
  dire, quant = line.split(" ")
  quant = int(quant)
  print(line)
  for i in range(quant):
    if dire == "U":
      H_pos[0] -= 1
    elif dire == "D":
      H_pos[0] += 1
    elif dire == "L":
      H_pos[1] -= 1
    else:
      H_pos[1] += 1
    if H_pos[0] < 0 or H_pos[0] >= dim:
      print("Error", H_pos)
      exit(1)
    if H_pos[1] < 0 or H_pos[1] >= dim:
      print("Error", H_pos)
      exit(1)
    vert = H_pos[0] - T_pos[0]
    hori = H_pos[1] - T_pos[1]
    need_update = abs(vert) >= 2 or abs(hori) >= 2
    # print(need_update)
    if need_update:
      # Same row or column
      if vert > 0:
        T_pos[0] += 1
      elif vert < 0:
        T_pos[0] -= 1
      if hori > 0:
        T_pos[1] += 1
      elif hori < 0:
        T_pos[1] -= 1
      tail_visited[T_pos[0]][T_pos[1]] = True

# print(tail_visited)

n_true = 0
for line in tail_visited:
  n_true += sum(line)

print(n_true)