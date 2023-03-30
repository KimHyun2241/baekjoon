import sys
input = sys.stdin.readline

book_count, book_pack = map(int, input().split())
A = True # 책의 순서가 맞는지 판별할 때 사용

for _ in range(book_pack): # 2더미 만큼 반복
    book_flow = int(input()) # 2더미로 나눈 한 더미에서의 책의 층
    book_num = list(map(int, input().split())) # 쌓인 책의 번호
    for j in range(book_flow-1): # 책의 층 만큼 비교
        if book_num[j] < book_num[j+1]: # 숫자의 크기가 내림차순인지 비교
            A = False # 아닐 시 False
            break
    if not A: break # 위에서 이미 A=False 이므로 for 중지

print('Yes' if A else 'No')