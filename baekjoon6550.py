import sys
input = sys.stdin.readline

while True: #멈출때 까지 문자열 입력받음
    st = input().rstrip() #문자열 초기화
    if not st: #빈 문자열이면 break
        break
    s, t = st.split() #띄어쓰기 기준으로 s, t에 문자열 초기화
    A = 0 #맞으면 1로 변환됨
    cnt = 0 
    
    for i in range(len(t)): #같은 문자열인지 검사
        if t[i] == s[cnt]: #같은 문자열이면 cnt += 1
            cnt += 1
            if cnt == len(s): #s와 길이가 같다면 같은 문자열을 포함
                A = 1
                break
    
    if A == 1:
        print('Yes')
    else:
        print('No')