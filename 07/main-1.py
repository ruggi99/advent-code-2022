from anytree import Node, RenderTree, PreOrderIter

data = open("input.txt").read().splitlines()

root = Node("root", dir=True)
print(getattr(root, "size", None))

current_node = None

for line in data:
  is_command = line.startswith("$")
  if is_command:
    command = line[2:4]
    if command == "cd":
      dir = line[5:]
      if dir == "..":
        current_node = current_node.parent
      elif dir == "/":
        current_node = root
      else:
        current_node = Node(dir, current_node, dir=True)
    else:
      pass
  else:
    is_dir = (line[:3] == "dir")
    if is_dir:
      pass
    else:
      size, name = line.split(" ")
      Node(name, current_node, size=int(size))

# print(RenderTree(root))

sizes = []
for dir in PreOrderIter(root, filter_=lambda n: hasattr(n, "dir")):
  total_size = 0
  for file in PreOrderIter(dir, filter_=lambda n: hasattr(n, "size")):
    total_size += file.size
  sizes.append(total_size)

print(sum(filter(lambda n: n < 100_000, sizes)))