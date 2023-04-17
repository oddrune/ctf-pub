i = 0
for line in open("data.txt").readlines():
    print(line[i], end='')
    i += 1
print()
