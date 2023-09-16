a, b = map(int, input().split())

def calcGCD(a, b):
    if a < b: # a가 더 크도록
        a, b = b, a
    r = a%b
    if r == 0:
        return b
    else:
        return calcGCD(b, r)

def calcLCM(a, b, c):
    return a*b//c

GCD = calcGCD(a,b)

print(calcGCD(a,b))
print(calcLCM(a, b, GCD))


    
