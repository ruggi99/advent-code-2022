with open("input.txt") as f:
  data = f.read().splitlines()

for i, line in enumerate(data):
  data[i] = list(map(int, line))

scores = []
for i, line in enumerate(data):
  for x in range(0, len(line)):
    height = line[x]
    visi = 0
    score = 1
    for t in range(0, i)[::-1]:
      if data[t][x] >= height:
        score *= (i - t)
        break
    else:
      score *= i
      visi += 1
    for t in range(0, x)[::-1]:
      if line[t] >= height:
        score *= (x - t)
        break
    else:
      score *= x
      visi += 1
    for t in range(i + 1, len(line)):
      if data[t][x] >= height:
        score *= (t - i)
        break
    else:
      score *= (len(data) - i - 1)
      visi += 1
    for t in range(x + 1, len(line)):
      if line[t] >= height:
        score *= (t - x)
        break
    else:
      score *= (len(line) - x - 1)
      visi += 1
    if visi > 0:
      scores.append(score)

print(sorted(scores)[-1])
