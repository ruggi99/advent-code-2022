with open("input.txt") as f:
  data = f.read().splitlines()

for i, line in enumerate(data):
  data[i] = list(map(int, line))

visible = 0
for i, line in enumerate(data):
  if i == 0 or i == len(data) - 1:
    visible += len(line)
    continue
  visible += 2
  for x in range(1, len(line) - 1):
    height = line[x]
    visi = 0
    for t in range(0, i):
      if data[t][x] >= height:
        break
    else:
      visi += 1
    for t in range(0, x):
      if line[t] >= height:
        break
    else:
      visi += 1
    for t in range(i + 1, len(line)):
      if data[t][x] >= height:
        break
    else:
      visi += 1
    for t in range(x + 1, len(line)):
      if line[t] >= height:
        break
    else:
      visi += 1
    if visi > 0:
      visible += 1

print(visible)