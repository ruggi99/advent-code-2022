data = open("input.txt").read().splitlines()[0]


for i in range(len(data)):
    marker = data[:14]
    for x in marker:
        if marker.count(x) != 1:
            break
    else:
        print(i + 14)
        break
    data = data[1:]
