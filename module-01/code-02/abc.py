table=[["A", "B", "C", "D", "E", "F", "G"],
    ["H", "I", "J", "K", "L", "M", "N"],
    ["O", "P", "Q", "R", "S", "T", "U"]]

for i in [0,1,2]:
    for j in [0,1,2,3,4,5,6]:
        print(table[i][j]+" ", end="")
    print()

while True:
    i = input("I:")
    j = input("J:")
    i = int(i)
    j = int(j)
    print("--->{}<---".format(table[i][j]))