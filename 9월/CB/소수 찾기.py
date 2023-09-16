n = int(input())

temp_list = list(map(int, input().split()))

ans = 0
for n in temp_list:
    if n == 1: continue
    flag = True
    for i in range(2, n//2+1):
        if n%i == 0:
            flag = False
            break
    if flag == True:
        ans += 1
        
print(ans)