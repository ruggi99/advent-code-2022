from collections import deque

with open("input.txt") as f:
  data = f.read().splitlines()

lines = [(i, int(line)) for i, line in enumerate(data)]

queue = deque(lines)
for i in range(len(data)):
  curr_idx = queue.index(lines[i])
  queue.remove(lines[i])
  orig_idx, number = lines[i]
  assert orig_idx == i

  new_idx = (curr_idx + number) % (len(data) - 1)

  queue.insert(new_idx, lines[i])

idx_0 = queue.index((data.index("0"), 0))
print(idx_0)
number_1000 = queue[(idx_0 + 1000) % len(data)]
number_2000 = queue[(idx_0 + 2000) % len(data)]
number_3000 = queue[(idx_0 + 3000) % len(data)]

print(number_1000[1] + number_2000[1] + number_3000[1])
