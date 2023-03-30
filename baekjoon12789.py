cnt = int(input()) # 숫자 갯수 입력
list_a = list(map(int, input().split())) # 숫자 리스트 입력 (대기줄)
list_b = [] # 다른 대기 줄
i = 1
while cnt:
    # list_a index 0이 i 인지 판별 and 빈 리스트인지 판별
    if len(list_a) != 0 and i == list_a[0]:
        list_a.pop(0)
        if i == cnt:
            print("Nice")
            exit()
        i += 1
    # list_a index -1이 i인지 판별 and 빈 리스트인지 판별
    elif len(list_b) != 0 and i == list_b[-1]:
        list_b.pop()
        if i == cnt:
            print("Nice")
            exit()
        i += 1
    # 두 리스트 0번과 -1번에 원하는 값이 없다면 추가 후 제거
    else:
        if not list_a: # list_a가 비어 있으면 종료
            print("Sad")
            exit()
        list_b.append(list_a.pop(0))