import sys
input = sys.stdin.readline
number = int(input()) #학기가 몇 분인지 정수 입력
count_num = []
sumPoint = 0 # 과제 점수 합
for i in range(number):
      count_num.insert(0, list(map(int, input().split()))) # i번 째 리스트에 리스트를 추가

      if count_num[0][0] == 1:
            count_num[0][2] -= 1

            if count_num[0][2] == 0:
                  sumPoint += count_num[0][1]
                  count_num.pop(0)
                  count_num[0][2] -= 1
      else:
            count_num.pop(0)
            count_num[0][2] -= 1
            
      if count_num[0][2] == 0:
            sumPoint += count_num[0][1]
            count_num.pop(0)
            count_num[0][2] -= 1

print(sumPoint)