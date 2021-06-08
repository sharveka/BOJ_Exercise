#가장 긴 증가하는 부분 수열의 길이

import sys
n=int(sys.stdin.readline())
array=[int(x) for x in sys.stdin.readline().split()]

# 메모 테이블 초기화
dp=[1]*n

for i in range(1, n):
    for j in range(0, i):
        if(array[j]<array[i]):
            dp[i]=max(dp[i], dp[j]+1)

result=0
for i in range(n):
    result=max(result, dp[i])

print(result)


'''
https://www.acmicpc.net/problem/11053
입력 예시
6
10 20 10 30 20 50

출력 
4

'''