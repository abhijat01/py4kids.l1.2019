kids=["Prateek", "Svadrut", "Meghna", "Sanjana", "Ishaan", "Sid", "Ari" ]

print(kids[0] )
print(kids[4])

for each_kid in kids:
    print("The kid is : {}".format(each_kid))

kids.append("Shloak")

for each_kid in kids:
    print("-----  {}  --------".format(each_kid))

number_of_kids = len(kids)
print("Number of kids : {}".format(number_of_kids))

for i in range(5):
    print(i)

import time

start_time = time.time()
for i in range(1000000):
    for j in range(1000):
        pass

end_time = time.time()
time_taken = end_time - start_time
print("Time taken:{}".format(time_taken))