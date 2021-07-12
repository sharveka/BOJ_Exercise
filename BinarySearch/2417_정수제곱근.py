import math
n=int(input())

start=0
end=n

while start<=end:
    mid=(start+end)//2

    if mid**2>=n:
        end=mid-1
        answer=mid
    else:
        start=mid+1

print(answer)

'''
https://www.acmicpc.net/problem/2417


입력 예시
122333444455555

출력
11060446

'''