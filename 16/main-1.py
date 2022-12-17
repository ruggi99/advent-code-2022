from itertools import combinations
import re

with open("input.txt") as f:
  data = f.read().splitlines()

for i, line in enumerate(data):
  data[i] = re.match("Valve (\w{2}) has flow rate=([0-9]+); tunnels? leads? to valves? (.*)$", line).group(1, 2, 3)

valves = {}
valves_pos = {}
for valve in data:
  name = valve[0]
  flow = int(valve[1])
  tunnels = valve[2].split(", ")
  valves[name] = {"name": name, "flow": flow, "tunnels": tunnels}
  if flow > 0:
    valves_pos[name] = {"name": name, "flow": flow, "tunnels": tunnels}

def calc_distance(first, last, _visited = []):
  valve_first = valves[first]
  tunnels = valve_first["tunnels"]
  if len(_visited) == 0:
    _visited.append(first)
  if last in tunnels:
    return 1
  distances = []
  visited = []
  for child in tunnels:
    if child in _visited:
      continue
    visited.append(child)
    distance = calc_distance(child, last, _visited + visited)
    if distance > 0:
      distances.append(distance)
  return 0 if len(distances) == 0 else sorted(distances)[0] + 1

# print(calc_distance("BB", "JJ"))
print(calc_distance("PY", "EB"))
distances = {}

for first, last in combinations(["AA"] + list(valves_pos.keys()), 2):
  distance = calc_distance(first, last)
  if distance == 0:
    print("Error", first, last)
    exit(1)
  distances[f'{first}{last}'] = distance
  distances[f'{last}{first}'] = distance


scores = []
TIME = 30

keys = set(valves_pos.keys())
print(keys)

def check_paths(time, last_valve, opened):
  opened.add(last_valve)
  remaining_paths = keys - opened
  scores = []
  for valve in remaining_paths:
    distance = distances[f'{last_valve}{valve}']
    if time + distance + 1 > TIME:
      continue
    _time = time + distance + 1
    _opened = opened.copy()
    score = valves[valve]["flow"] * (TIME - _time) + check_paths(_time, valve, _opened)
    scores.append(score)
  return 0 if len(scores) == 0 else sorted(scores)[-1]


score = check_paths(0, "AA", set())
print(score)
