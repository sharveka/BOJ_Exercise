#가장 긴 증가하는 부분 수열
n=int(input())
array=list(map(int, input().split()))

#가장 긴 증가하는 부분 수열 문제로 바꿔주기 위해 오름차순 정렬
array.reverse()

#memoization
dp=[1]*n

for i in range(1, n):
    for j in range(0,i):
        if array[j]<array[i]:
            dp[i]=max(dp[i], dp[j]+1)


print(n-max(dp))


'''
https://www.acmicpc.net/problem/18353
입력 예시
7
15 11 4 8 5 2 4

출력
2
'''