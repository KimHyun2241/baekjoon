import sys
input = sys.stdin.readline
print("input 변수 할당")

n, m = map(int, input().split())
# 4 2
p = True
for _ in range(m): # 4
    i = int(input())
    # 2
    k = list(map(int, input().split()))
    # 3 1
    for j in range(i-1): # 0, 1 반복
        if k[j] < k[j+1]: #3이 1보다 작으면 
            p = False
            break
    if not p: break # False로 할당?

print('Yes' if p else 'No') # True이면 Yes 아니면 False 출력?