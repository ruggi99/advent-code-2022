data = open("input.txt").read()[:-1]
array = data.split("\n\n")
for i, val in enumerate(array):
  array[i] = val.split("\n")
for i, val in enumerate(array):
  array[i] = sum(map(int, val))

one = max(array)
array.remove(one)
second = max(array)
array.remove(second)
third = max(array)
array.remove(third)

print(one + second + third)
