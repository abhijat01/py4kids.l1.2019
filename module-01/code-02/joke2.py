p1="Why did the student eat his homework"
p2="Because the teacher told him it was a piece of cake"

words = p1.split()+p2.split()
print(len(words))

words = [ " "+x for x in words]


mat = []
m,n=3,7
answer = []
for _ in range(m):
    row = []
    for __ in range(n):
        row.append(" ")
    mat.append(row)

import numpy as np
random_idx = np.random.choice(m*n-1, len(words), replace=False)
print(random_idx)
for num in random_idx:
    i ,j= num//n , num%n
    w = words.pop()
    mat[i][j] = w
    answer.append((i,j))
    print("mat[{}][{}] = '{}'".format(i,j,w))
mat[m-1][n-2] = "?\n"
mat[m-1][n-1] = "!\n"


print("----------------")
for i in range(m):
    for j in range(n):
        print("{:8s}".format(mat[i][j]), end=" ")
    print()

print(reversed(answer))
for i,j in reversed(answer):
    print("([{}][{}]) ".format(i,j) , end="")
print()

for i,j in reversed(answer):
    print(mat[i][j], end="")
