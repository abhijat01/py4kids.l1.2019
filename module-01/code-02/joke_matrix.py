def make_joke_puzzle():
    mat = []
    m,n=3,7
    answer = []
    for _ in range(m):
        row = []
        for __ in range(n):
            row.append(" ")
        mat.append(row)

    mat[1][3] = ' cake'
    mat[2][5] = ' of'
    mat[1][6] = ' piece'
    mat[2][3] = ' a'
    mat[0][2] = ' was'
    mat[2][2] = ' it'
    mat[0][3] = ' him'
    mat[1][2] = ' told'
    mat[0][5] = ' teacher'
    mat[1][0] = ' the'
    mat[2][1] = ' Because'
    mat[0][1] = ' homework'
    mat[0][6] = ' his'
    mat[1][4] = ' eat'
    mat[2][0] = ' student'
    mat[1][1] = ' the'
    mat[2][4] = ' did'
    mat[1][5] = ' Why'
    mat[0][0] = ' piece'
    mat[1][6] = '?\n'
    mat[2][6]  = '!\n'
    return mat

def print_joke_table(table, m, n):
    for i in range(m):
        for j in range(n):
            word = table[i][j]
            print("{:8s}".format(word), end=" ")
        print()

def print_answer(joke_table, answer_seq):
    for location in answer_seq:
        i = location[0]
        j = location[1]
        print(joke_table[i][j], end="")
    print()

joke_table = make_joke_puzzle()
print_joke_table(joke_table, 3, 7)
answer_sequence = [(1,5), (2,4),(1,0), ( 2,0)]
print_answer(joke_table,answer_sequence)

import date
print(date.today)