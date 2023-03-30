import sys
input = sys.stdin.readline

N = int(input()) # 1 A T: 과제O, 점수, 걸린 시간
count_num = []
score = 0
for _ in range(N):
    info = list(map(int, input().split()))
    if info[0] == 1:  # 첫번째 입력값이 1이면 과제를 받음
        if info[2] - 1 > 0: # 시간에서 -1
            count_num.append((info[1], info[2] - 1)) #리스트에 튜플을 저장
        else:
            score += info[1] # 시간에서 -1 = 0 일 경우 과제 완료
    else:  # 과제 없음
        if count_num:
            pop_tuple = count_num.pop() #리스트에 저장된 튜플을 꺼내서 pop_tuple로 저장
            if pop_tuple[1] - 1 > 0: # 시간이 0보다 크면 시간 -1 을 하고 다시 count_num 리스트에 추가
                count_num.append((pop_tuple[0], pop_tuple[1] - 1))
            else:
                score += pop_tuple[0] # 시간에서 -1 = 0 일 경우 과제 완료

print(score)