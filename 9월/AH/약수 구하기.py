N, K = map(int, input().split()) # 입력값

num_list = [] # 약수 담을 리스트

if K == 1: # K가 1이면 무조건 1 return
    print(1)
    exit()

for i in range(1, N+1): # 약수 구하기
    if N % i == 0:
        num = N // i
        num_list.append(num)

num_list.sort() # 정렬

if len(num_list) < K: # 약수 개수보다 K가 크면 0 출력
    print(0)
else:
    print(num_list[K-1])