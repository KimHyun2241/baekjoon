import sys
input = sys.stdin.readline

# 막대기 수 입력
stick = int(sys.stdin.readline())
list_a = []

for i in range(stick):
    # 막대기 크기 입력
    num = int(sys.stdin.readline())

    # 리스트가 비어 있고 리스트의 제일 오른쪽이 입력 받은 값보다 작을 경우
    while list_a and list_a[-1] <= num:
        # 리스트의 수가 입력 값보다 작을 경우
        list_a.pop()
    #리스트에 추가
    list_a.append(num)
answer = len(list_a)
print(answer)

##########################################################################

import sys
input = sys.stdin.readline

stick = int(input()) # 막대기 갯수
list_a = [] # 입력받은 막대기
list_b = [] # 마지막 막대기 보다 긴 막대기들
i = 0 # while에 사용

while i < stick: # 막대기 갯수 만큼 while 반복
        number = int(input())
        list_a.append(number)
        i += 1
for i in range(stick):
    if list_a[-1] < list_a[-i-1]: # 오른쪽에서 왼쪽으로 마지막 막대기와 길이 비교
        if list_a[-i-1] == max(list_a): # 가장 긴 막대기가 나오면 list_b에 추가 후 break
            list_b.append(list_a[-i-1])
            break
        list_b.append(list_a[-i-1]) # 마지막 막대기보다 긴 막대기 list_b에 추가
if len(list_b) == 0: # list_b가 비어 있다면 0 출력
     print(0)
else:
     print(len(set(list_b))+1) # 중복값을  set함수로 정리 후 +1한 후 출력