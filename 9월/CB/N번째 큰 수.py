t = int(input())
for _ in range(t):
    temp_list = list(map(int, input().split()))
    temp_list.sort()
    print(temp_list[-3])

