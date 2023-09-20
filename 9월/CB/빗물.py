h, w = map(int, input().split())

block_heights = list(map(int, input().split()))

blocks = [[] for i in range(h)]
for i in block_heights:
    for j in range(h):
        if j < i:
            blocks[j].append(1)
        else:
            blocks[j].append(0)

ans = 0
for i in range(len(blocks)): # [[1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 1, 1], [1, 1, 1, 1]]
    if 0 in blocks[i] :
        
        flag = False
        temp_cnt = 0
        for j in range(len(blocks[i])): # 0~3
            if blocks[i][j] == 1:
                if flag == False:
                    flag = True
                else:
                    ans += (temp_cnt)
                    temp_cnt = 0
                    flag = True
            else:
                if flag == True:
                    temp_cnt += 1

print(ans)






                

                


                    



        

                    

        

