
h_list = []
for _ in range(9):
    h_list.append(int(input()))

h_list.sort()
answer = []
for i in range(9):
    for j in range(9):
        if i == j: continue
        temp_list = [k for k in h_list]
        temp_list.remove(h_list[i]); temp_list.remove(h_list[j])
        if sum(temp_list) == 100:
            answer = temp_list
            break
    if len(answer) != 0:
        break

for i in answer:
    print(i)