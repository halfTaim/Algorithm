n = int(input())

num_list = [0, 1]

if n == 0:
    print(0)
    exit()
elif n == 1:
    print(1)
    exit()

for i in range(1, n):
    num_list.append(num_list[i-1] + num_list[i])

print(num_list[-1])