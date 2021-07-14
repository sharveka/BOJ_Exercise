# 퇴사 날짜부터 거꾸로 확인

import sys
input=sys.stdin.readline
n=int(input())
t=[]    # 각 상담을 완료하는데 걸리는 기간
p=[]    # 각 상담을 완료했을 때 받는 금액
dp=[0]*(n+1)    # memoization
max_value=0

for _ in range(n):
    x,y=map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n-1, -1, -1):
    time=t[i]+i

    # 상담이 기간안에 끝난다
    if time<=n:
        dp[i]=max(p[i]+dp[time], max_value)
        max_value=dp[i]

    # 상담이 기간을 벗어나는 경우
    else:
        dp[i]=max_value

print(max_value)



'''
https://www.acmicpc.net/problem/14501

입력 예시
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

출력 
45
ㅡ
'''