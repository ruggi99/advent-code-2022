import math

with open("input.txt") as f:
  data = f.read().split("\n\n")

monkeys = []

class Monkey:
  def __init__(self, items, op, test, m_true, m_false) -> None:
    self.items = items
    self.op = op
    self.test = test
    self.m_true = m_true
    self.m_false = m_false
    self.count = 0

for inst in data:
  inst = inst.split("\n")
  n_monkey = int(inst[0][7:-1])
  items = list(map(int, inst[1][18:].split(", ")))
  op = inst[2][19:]
  test = int(inst[3][21:])
  m_true = int(inst[4][29:])
  m_false = int(inst[5][30:])
  monkeys.append(Monkey(items, op, test, m_true, m_false))

# Divide each worry level by the least common multiple
base = math.lcm(*[m.test for m in monkeys])
print(base)

for i in range(10000):
  for m in monkeys:
    for old in m.items:
      new = eval(m.op)
      new %= base
      if new % m.test:
        monkeys[m.m_false].items.append(new)
      else:
        monkeys[m.m_true].items.append(new)
      m.count += 1
    m.items.clear()
      
times = []
for m in monkeys:
  times.append(m.count)
  print(m.__dict__)

times = sorted(times, reverse=True)

print(times[0] * times[1])
