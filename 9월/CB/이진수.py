t = int(input())
for _ in range(t):
    n = int(input())
    ss = str(bin(n)).lstrip('0b')
    ss = list(reversed(ss))
    answer = []
    for i in range(len(ss)):
        if ss[i] == '1':
            answer.append(i)

    for i in answer:
        print(i, end=' ')
    print()
