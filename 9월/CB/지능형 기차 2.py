
numOfHuman = []
for _ in range(10):
    outputs, inputs = map(int, input().split())
    if len(numOfHuman) == 0:
        numOfHuman.append(inputs)
    else:
        numOfHuman.append(numOfHuman[-1]-outputs+inputs)

print(max(numOfHuman))

