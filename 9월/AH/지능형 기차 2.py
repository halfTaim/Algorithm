rows = 10
cols = 2

num_list = [list(map(int, input().split())) for _ in range(rows)]

max_tmp = num_list[0][1]
rest_people = num_list[0][1]

for idx in range(1, rows):
    rest_people -= num_list[idx][0]
    add_people = num_list[idx][1]
    total = rest_people + add_people
    if max_tmp < total:
        max_tmp = total
    rest_people = total

print(max_tmp)