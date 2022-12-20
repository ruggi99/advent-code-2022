import re
import json
from copy import deepcopy

with open("input.txt") as f:
  data = f.read().splitlines()

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
    pass

blueprints: list[Blueprint] = []

for line in data:
  blueprints.append(Blueprint(*line))

class State:
  def __init__(self, bp: Blueprint) -> None:
    self.bp = bp
    self.ore_robot_count = 1
    self.clay_robot_count = 0
    self.obs_robot_count = 0
    self.geode_robot_count = 0
    self.ore_robot_count_const = 0
    self.clay_robot_count_const = 0
    self.obs_robot_count_const = 0
    self.geode_robot_count_const = 0
    self.ore = 0
    self.clay = 0
    self.obs = 0
    self.geode = 0
  
  def mine(self):
    self.ore += self.ore_robot_count
    self.clay += self.clay_robot_count
    self.obs += self.obs_robot_count
    self.geode += self.geode_robot_count
  
  def construct_ore_robot(self):
    ore_needed = self.bp.ore_per_ore_robot
    if self.ore >= ore_needed:
      self.ore -= ore_needed
      self.ore_robot_count_const += 1
      return True
    return False
  
  def construct_clay_robot(self):
    ore_needed = self.bp.ore_per_clay_robot
    if self.ore >= ore_needed:
      self.ore -= ore_needed
      self.clay_robot_count_const += 1
      return True
    return False
    
  def construct_obs_robot(self):
    ore_needed = self.bp.ore_per_obs_robot
    clay_needed = self.bp.clay_per_obs_robot
    if self.ore >= ore_needed and self.clay >= clay_needed:
      self.ore -= ore_needed
      self.clay -= clay_needed
      self.obs_robot_count_const += 1
      return True
    return False
    
  def construct_geode_robot(self):
    ore_needed = self.bp.ore_per_obs_robot
    obs_needed = self.bp.obs_per_geode_robot
    if self.ore >= ore_needed and self.obs >= obs_needed:
      self.ore -= ore_needed
      self.obs -= obs_needed
      self.geode_robot_count_const += 1
      return True
    return False
  
  def finish(self):
    self.ore_robot_count += self.ore_robot_count_const
    self.clay_robot_count += self.clay_robot_count_const
    self.obs_robot_count += self.obs_robot_count_const
    self.geode_robot_count += self.geode_robot_count_const
    self.ore_robot_count_const = 0
    self.clay_robot_count_const = 0
    self.obs_robot_count_const = 0
    self.geode_robot_count_const = 0
  
  def __str__(self) -> str:
    tmp = self.__dict__.copy()
    del tmp["bp"]
    return json.dumps(tmp)


qualities = []

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

  def _run(state: State, strategy: str, time: int):
    def construct(state: State, strategy: str, time: int):
      if time > 1 and state.construct_geode_robot():
        return
      if time > 2 and state.construct_obs_robot():
        return
      if time < 5:
        return
      if strategy == "ore":
        state.construct_ore_robot()
      elif strategy == "clay":
        state.construct_clay_robot()
    construct(state, strategy, time)
    state.mine()
    state.finish()
    return state

  def get_key(state: State):
    return (
      state.ore,
      state.clay,
      state.obs,
      state.geode,
      state.ore_robot_count,
      state.clay_robot_count,
      state.obs_robot_count,
      state.geode_robot_count
    )

  strategies = ["ore", "clay", "none"]

  geodes: list[int] = []
  for bp in blueprints:
    state = State(bp)
    states: list[State] = [state]
    states_next: list[State] = []
    obs_optimized = False
    for t in range(24, 0, -1):
      cache = {}
      print(t)
      for st in list(states):
        states.remove(st)
        for strat in strategies:
          if st.obs > 0 or st.geode > 0:
            if strat == "ore":
              continue
          cp = copy_state(st)
          _run(cp, strat, t)
          states_next.append(cp)
      _geodes = [_st.geode for _st in states_next]
      _geodes_max = max(_geodes)
      if not obs_optimized:
        _obss = [_st.obs for _st in states_next]
        _obss_max = max(_obss)
      for st in states_next:
        key = get_key(st)
        if cache.get(key, False):
          continue
        cache[key] = True
        if st.geode == _geodes_max:
          states.append(st)

      print(len(states_next), len(states), _geodes_max)
      states_next.clear()
    geodes.append(states[0].geode)
  
  quality = 0
  for i, bp in enumerate(blueprints):
    quality += bp.id * geodes[i]

  print(geodes)
  print(quality)

run()
