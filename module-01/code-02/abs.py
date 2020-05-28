table=[["A", "B", "C", "D", "E", "F", "G"],
    ["H", "I", "J", "K", "L", "M", "N"],
    ["O", "P", "Q", "R", "S", "T", "U"]]

for i in range(3):
    for j in range(7):
        print(table[i][j]+" ", end="")
    print()