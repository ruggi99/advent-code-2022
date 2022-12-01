data = open("input.txt").read()[:-1]
array = data.split("\n\n")
for i, val in enumerate(array):
  array[i] = val.split("\n")
for i, val in enumerate(array):
  array[i] = sum(map(int, val))

print(max(array))
