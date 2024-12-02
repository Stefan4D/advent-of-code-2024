input_file = 'input.txt'

list_a: list = []
list_b: list = []
total_distance = 0

with open(input_file, 'r') as file:
    lines = file.readlines()
    for line in lines:
        ln = line.split(" ", 1)
        list_a.append(int(ln[0].strip()))
        list_b.append(int(ln[1].strip()))

list_a.sort()
list_b.sort()

for x in range(len(list_a)):
    if list_a[x] > list_b[x]:
        total_distance += list_a[x] - list_b[x]
    else:
        total_distance += list_b[x] - list_a[x]

print(total_distance)
# print(len(list_a))
# print(len(list_b))

# ************
# Part 2
# ************

similarity_dict: dict = {}
sim_score = 0

# for x in range(len(list_a)):
#     if list_a[x] in similarity_dict:
#         sim_score += similarity_dict[list_a[x]]
#     else:
#         similarity_dict[list_a[x]] = list_a[x] * list_b.count(list_a[x])
#         sim_score += similarity_dict[list_a[x]]

for x in range(len(list_a)):
    sim_score += list_b.count(list_a[x]) * list_a[x]

print(sim_score)