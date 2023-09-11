T = int(input()) # 테스트 케이스

for _ in range(T): # 테스트 케이스만큼 반복
    n = int(input()) # 이진수로 바꿀 숫자 입력
    num_list = [] # 인덱스 저장할 리스트
    cnt = -1 # count
    while True: # 일단 반복
        if n == 1: # 이진수 변환 끝 -> while 탈출
            cnt += 1 # 인덱스 count
            num_list.append(cnt) # 인덱스 리스트에 추가
            break
        if n % 2 == 0: # 0이면 인덱스 count만 증가
            cnt += 1
        else: # 1이면 인덱스 count 및 리스트에 인덱스 추가
            cnt += 1
            num_list.append(cnt)
        n //= 2

    print(" ".join(map(str, num_list))) # 나열