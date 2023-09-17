m = int(input())
n = int(input())

prime_list = []
for num in range(m, n+1):
    flag = True
    for i in range(2, num//2+1):
        if num%i == 0:
            flag = False
            break
    if flag:
        prime_list.append(num)

if m == 1:
    prime_list.remove(1)
if len(prime_list) == 0:
    print(-1)
else:
    print(sum(prime_list))
    print(prime_list[0])
