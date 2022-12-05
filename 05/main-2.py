import math

data = open("input.txt").read().splitlines()

nstacks = math.ceil(len(data[0]) / 4)

stacks = [[] for i in range(nstacks)]

while data[0] != "":
  line = data.pop(0)
  for i in range(nstacks):
    crate = line[i*4+1:i*4+2]
    if not crate.isupper():
      continue
    stacks[i].append(crate)

data.pop(0)

for line in data:
  quantity = int(line[5:7])
  start = int(line[12:14]) - 1
  end = int(line[17:19]) - 1
  for i in range(quantity):
    stacks[end].insert(i, stacks[start].pop(0))

final_str = ""
for stack in stacks:
  final_str += stack[0]

print(final_str)