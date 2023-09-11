# 1
# 01
# 1001
# 01101001
# 1001011001101001
# 01101001100101101001011001101001
# 1001011001101001011010011001011001101001100101101001011001101001
#

# 0

# 1
# 1 1*2 -1
# 3 1*2 +1
# 5 3*2 -1
# 11 5*2 +1

def zigzag(num, n, end):
    new_num = num*2
    if n%2 == 0:
        new_num -= 1
    else:
        new_num += 1
    n += 1
    if n < end:
        return zigzag(new_num, n, end)
    else:
        return new_num

n = int(input())

if n == 1:
    print(0)
elif n == 2:
    print(1)
elif n == 3:
    print(1)
else:
    print(zigzag(1, 1, n-2))







