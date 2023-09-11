n, k = map(int, input().split())

divisors = []
for i in range(1, n//2+1):
    if n%i == 0: divisors.append(i)
    if len(divisors) == k: break
divisors.append(n)
try:
    print(divisors[k-1])
except:
    print(0)