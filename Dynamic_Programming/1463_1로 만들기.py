# 다이나믹 프로그래밍 Bottom up


n=int(input())

#DP테이블 초기화
d=[0]*(n+1)
d[1]=0

#Bottom up Dynamic
for i in range(2, n+1):
    # 현재의 수에서 1을 빼는 경우
    d[i]=d[i-1]+1

    #현재 수가 2로 나누어 떨어지는 경우
    if i%2==0:
        d[i]=min(d[i], d[i//2]+1)

    #현재 수가 3로 나누어 떨어지는 경우
    if i%3==0:
        d[i]=min(d[i], d[i//3]+1)

print(d[n])

'''
https://www.acmicpc.net/problem/1463

입력 예시
10

출력 
3
'''