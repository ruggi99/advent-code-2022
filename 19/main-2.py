import re
import json
from collections import deque

MAX_TIME = 32

with open("input.txt") as f:
  data = f.read().splitlines()

data = data[:3]

for i, line in enumerate(data):
  data[i] = re.match("Blueprint (\d*): Each ore robot costs (\d*) ore. Each clay robot costs (\d*) ore. Each obsidian robot costs (\d*) ore and (\d*) clay. Each geode robot costs (\d*) ore and (\d*) obsidian.", line).group(1, 2, 3, 4, 5, 6, 7)

class Blueprint:
  def __init__(self, id, ore_per_ore_robot, ore_per_clay_robot, ore_per_obs_robot, clay_per_obs_robot, ore_per_geode_robot, obs_per_geode_robot) -> None:
    self.id = int(id)
    self.ore_per_ore_robot = int(ore_per_ore_robot)
    self.ore_per_clay_robot = int(ore_per_clay_robot)
    self.ore_per_obs_robot = int(ore_per_obs_robot)
    self.clay_per_obs_robot = int(clay_per_obs_robot)
    self.ore_per_geode_robot = int(ore_per_geode_robot)
    self.obs_per_geode_robot = int(obs_per_geode_robot)
    self.max_ore_per_cycle = max(self.ore_per_ore_robot, self.ore_per_clay_robot, self.ore_per_obs_robot, self.ore_per_geode_robot)
    self.max_clay_per_cycle = self.clay_per_obs_robot
    self.max_obs_per_cycle = self.obs_per_geode_robot

blueprints: list[Blueprint] = []

for line in data:
  blueprints.append(Blueprint(*line))

# blueprints = blueprints[:1]

class State:
  def __init__(self, bp: Blueprint) -> None:
    self.bp = bp
    self.ore = 0
    self.clay = 0
    self.obs = 0
    self.geode = 0
    self.ore_robot_count = 1
    self.clay_robot_count = 0
    self.obs_robot_count = 0
    self.geode_robot_count = 0
    self.construction = None
  
  def mine(self):
    self.ore += self.ore_robot_count
    self.clay += self.clay_robot_count
    self.obs += self.obs_robot_count
    self.geode += self.geode_robot_count
    if self.construction == "ore":
      self.ore_robot_count += 1
    elif self.construction == "clay":
      self.clay_robot_count += 1
    elif self.construction == "obs":
      self.obs_robot_count += 1
    elif self.construction == "geode":
      self.geode_robot_count += 1
    self.construction = None
  
  def can_construct_ore_robot(self):
    if self.ore_robot_count >= self.bp.max_ore_per_cycle:
      return False
    ore_needed = self.bp.ore_per_ore_robot
    if self.ore < ore_needed:
      return False
    if self.ore > ore_needed * 2:
      return False
    return True
  
  def construct_ore_robot(self):
    if not self.can_construct_ore_robot():
      return False
    ore_needed = self.bp.ore_per_ore_robot
    self.ore -= ore_needed
    self.construction = "ore"
    return True
  
  def can_construct_clay_robot(self):
    if self.clay_robot_count >= self.bp.max_clay_per_cycle:
      return False
    ore_needed = self.bp.ore_per_clay_robot
    if self.ore < ore_needed:
      return False
    if self.ore > ore_needed * 2:
      return False
    return True
  
  def construct_clay_robot(self):
    if not self.can_construct_clay_robot():
      return False
    ore_needed = self.bp.ore_per_clay_robot
    self.ore -= ore_needed
    self.construction = "clay"
    return True
  
  def can_construct_obs_robot(self):
    if self.obs_robot_count >= self.bp.max_obs_per_cycle:
      return False
    ore_needed = self.bp.ore_per_obs_robot
    clay_needed = self.bp.clay_per_obs_robot
    if self.ore < ore_needed or self.clay < clay_needed:
      return False
    if self.ore > ore_needed * 2 and self.clay > clay_needed * 2:
      return False
    return True

  def construct_obs_robot(self):
    if not self.can_construct_obs_robot():
      return False
    ore_needed = self.bp.ore_per_obs_robot
    clay_needed = self.bp.clay_per_obs_robot
    self.ore -= ore_needed
    self.clay -= clay_needed
    self.construction = "obs"
    return True
    
  def can_construct_geode_robot(self):
    ore_needed = self.bp.ore_per_geode_robot
    obs_needed = self.bp.obs_per_geode_robot
    if self.ore < ore_needed or self.obs < obs_needed:
      return False
    return True

  def construct_geode_robot(self):
    if not self.can_construct_geode_robot():
      return False
    ore_needed = self.bp.ore_per_geode_robot
    obs_needed = self.bp.obs_per_geode_robot
    self.ore -= ore_needed
    self.obs -= obs_needed
    self.construction = "geode"
    return True
  
  def can_construct_all_robots(self):
    return self.can_construct_ore_robot() and self.can_construct_clay_robot() and self.can_construct_obs_robot() and self.can_construct_geode_robot()
  
  def calculate_max_geodes(self, remaining_time) -> int:
    achievable = self.geode_robot_count * remaining_time
    return self.geode + achievable + (remaining_time + 1) * remaining_time // 2
  
  def __str__(self) -> str:
    tmp = self.__dict__.copy()
    del tmp["bp"]
    return json.dumps(tmp)


def copy_state(st: State):
  state = State(st.bp)
  state.ore_robot_count = st.ore_robot_count
  state.clay_robot_count = st.clay_robot_count
  state.obs_robot_count = st.obs_robot_count
  state.geode_robot_count = st.geode_robot_count
  state.ore = st.ore
  state.clay = st.clay
  state.obs = st.obs
  state.geode = st.geode
  return state


def run():
  def _run(state: State, time: int, max_geodes: int):
    if time == 0:
      return state.geode
    if time < 8:
      if (state.geode + state.calculate_max_geodes(time + 1)) < max_geodes:
        # print("Skip", max_geodes)
        return state.geode
    key = get_key(time, state)
    value = cache.get(key, 0)
    if value > state.geode:
      # print("ciao")
      return value
    cache[key] = state.geode
    states: list[State] = []
    if state.can_construct_ore_robot():
      cp = copy_state(state)
      cp.construct_ore_robot()
      states.append(cp)
    if state.can_construct_clay_robot():
      cp = copy_state(state)
      cp.construct_clay_robot()
      states.append(cp)
    if state.can_construct_obs_robot():
      cp = copy_state(state)
      cp.construct_obs_robot()
      states.append(cp)
    if state.can_construct_geode_robot():
      cp = copy_state(state)
      cp.construct_geode_robot()
      states.append(cp)
    if not state.can_construct_all_robots():
      cp = copy_state(state)
      states.append(cp)

    _max_geodes = max_geodes
    for st in states:
      st.mine()
      geode = _run(st, time - 1, _max_geodes)
      # if _max_geodes < geode:
      #   print("New max", geode)
      _max_geodes = max(_max_geodes, geode)
    return _max_geodes
  
  def get_key(time: int, state: State):
    return (
      time,
      state.ore,
      state.clay,
      state.obs,
      state.ore_robot_count,
      state.clay_robot_count,
      state.obs_robot_count,
      state.geode_robot_count,
    )

  geodes: list[int] = []
  for bp in blueprints:
    cache = {}
    state = State(bp)
    queue: deque[State] = deque()
    queue.append(state)
    queue_next: deque[State] = deque()
    max_geodes = 0
    for t in range(MAX_TIME):
      print("Minuto", t + 1)
      print(len(queue))
      while queue:
        state = queue.pop()
        if state.calculate_max_geodes(MAX_TIME - t - 1) < max_geodes:
          # print("upper bound")
          continue
        cp = copy_state(state)
        cp.mine()
        queue_next.append(cp)
        if t < 14 and state.can_construct_ore_robot():
          cp = copy_state(state)
          cp.construct_ore_robot()
          cp.mine()
          queue_next.append(cp)
        if t < 26 and state.can_construct_clay_robot():
          cp = copy_state(state)
          cp.construct_clay_robot()
          cp.mine()
          queue_next.append(cp)
        if state.can_construct_obs_robot():
          cp = copy_state(state)
          cp.construct_obs_robot()
          cp.mine()
          # if get_key(t - 1, state) == (19, 3, 14, 7, 2, 7, 4, 1):
          #   print("DEBUG")
          #   print(cp)
          queue_next.append(cp)
        if state.can_construct_geode_robot():
          cp = copy_state(state)
          cp.construct_geode_robot()
          cp.mine()
          queue_next.append(cp)
      # print(len(queue), len(queue_next))
      # print(queue_next)
      while queue_next:
        state = queue_next.popleft()
        max_geodes = max(max_geodes, state.geode)
        key = get_key(t, state)
        cache_geodes = cache.get(key, -1)
        if cache_geodes >= state.geode:
          # print("ciao")
          continue
        cache[key] = state.geode
        queue.append(state)
      # if t == 19:
      #   print(cache.get((19, 3, 14, 7, 2, 7, 4, 1), "Non trovato"))
      if t == 21:
        print(cache.get((21, 2, 14, 9, 2, 7, 5, 2), "Non trovato"))
      print(queue[-1])
      # queue = queue_next
      # queue_next = deque()
      # for st in queue:
      #   print(st)
      print(max_geodes)
      cache.clear()
    geodes.append(max_geodes)
  
  quality = 1
  for geo in geodes:
    quality *= geo

  print(geodes)
  print(quality)

run()
