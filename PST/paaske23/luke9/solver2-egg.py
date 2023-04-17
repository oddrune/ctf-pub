i = 0
for line in reversed(open("informasjon.txt").readlines()):
    print(line[i], end='')
    i += 1
print()
