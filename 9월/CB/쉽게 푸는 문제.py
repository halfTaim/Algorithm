a, b = map(int, input().split())

def whatNumIndex(n, index): 
    if int((1 + n)/2 * n) < index:
        return whatNumIndex(n+1, index)
    else:
        return n, int((1 + n)/2 * n)

temp_list = [i for i in range(1, whatNumIndex(1, b)[0]+1) for j in range(1, i+1)]
print(sum(temp_list[a-1:b]))

