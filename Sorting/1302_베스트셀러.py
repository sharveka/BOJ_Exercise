# Dictionary 활용
# 참고 : https://wikidocs.net/16 

import sys
input=sys.stdin.readline

n=int(input())
books={}    # dictionary 선언

for _ in range(n):
    book=input().rstrip()

    if book not in books:
        books[book]=1       # 사전 자료형 접근법 - [key] 로 접근
    else: 
        books[book]+=1


max_cnt=max(books.values()) # 사전 자료형 value 에 접근
best=[]

for book, count in books.items():   # key, value 쌍 얻기 
    if count==max_cnt:
        best.append(book)

print(sorted(best)[0])        



'''
Python Dictionary Method
https://wikidocs.net/16#key-value-items


https://www.acmicpc.net/problem/1302

입력예시

5
top
top
top
top
kimtop

출력
top

'''