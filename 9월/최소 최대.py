N = int(input())

num_list = list(map(int, input().split()))
max_tmp, min_tmp = num_list[0], num_list[0]

for idx in range(1, N+1):
    if num_list[idx-1] < min_tmp:
        min_tmp = num_list[idx-1]
    elif num_list[idx-1] > max_tmp:
        max_tmp = num_list[idx-1]

print(min_tmp, max_tmp)