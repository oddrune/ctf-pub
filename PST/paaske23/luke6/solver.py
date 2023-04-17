base9 = [[101, 148, 35, 103, 80, 146, 102, 72, 76,],
        [80, 103, 102, 148, 76, 72, 101, 88, 146,],
        [76, 72, 146, 101, 88, 35, 148, 35, 80,],
        [148, 88, 76, 72, 101, 103, 80, 146, 102,],
        [35, 80, 72, 102, 148, 88, 103, 76, 101,],
        [103, 102, 101, 76, 146, 35, 35, 148, 88,],
        [88, 146, 148, 80, 103, 101, 76, 102, 72,],
        [72, 35, 103, 146, 102, 35, 88, 80, 35,],
        [102, 76, 80, 88, 72, 148, 146, 101, 103],]

# Konverter til bokstaver
chars = []
for line in base9:
    chars.append([chr(int(str(x),9)) for x in line])

# Finner alfabetet
abc = set([ch for line in chars for ch in line]) - set(" ")

# Reformater til sudoku-hjørner (chatgpt-kode)
sudoku = [[0 for i in range(9)] for j in range(9)]
for i in range(9):
    for j in range(9):
        k = (i // 3) * 3 + (j // 3)
        sudoku[k][j % 3 + (i % 3) * 3] = chars[i][j]

# Printer manglende bokstav i hver blokk
for block in sudoku:
    print((abc - set(block)).pop(), end='')
print()