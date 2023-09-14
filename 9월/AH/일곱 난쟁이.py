from itertools import combinations

num_list = [int(input()) for _ in range(9)]

dwarf = list(combinations(num_list, 7))

for num in dwarf:
    if sum(num) == 100:
        print(*sorted(num), sep="\n")
        break