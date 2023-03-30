cnt = int(input()) # 숫자 갯수 입력
list_a = list(map(int, input().split())) # 숫자 리스트 입력
cnt = 0 # 킬 수 카운트
output_num = 0 # 킬 수
max_num = 0 # 리스트 내 가장 큰 수

for i in list_a: # 리스트 순서대로 비교
    if i > max_num: # 자신의 왼쪽의 숫자가 자신보다 클 경우
        max_num = i # 큰 숫자로 초기화
        cnt = 0 # 0으로 초기화
    else:
        cnt += 1 # 자신의 왼쪽의 숫자가 자신보다 작을 경우
    output_num = max(output_num, cnt) # 앞에 저장한 숫자와 현재 숫자 중 가장 큰 숫자로 초기화
print(output_num)