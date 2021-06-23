import sys
input = sys.stdin.readline

n,m=map(int, input().split())
maze=[]
for _ in range(n):
    maze.append(list(map(int, input().split())))

#다이나믹 프로그래밍 결과를 담을 dp테이블 초기화
dp=[]
dp=maze


#Bottom up Dynamic Programming
for i in range(n):
    for j in range(m):
        #왼쪽 위 대각선에서 오는 경우
        if i==0 or j==0:
            diagonal=0
        else:
            diagonal=dp[i-1][j-1]
    
        #왼쪽에서 오는 경우
        if j==0:
            left=0
        else:
            left=dp[i][j-1]

        #위쪽에서 오는 경우
        if i==0:
            up=0
        else:
            up=dp[i-1][j]

        dp[i][j]=dp[i][j]+max(diagonal, left, up)

print(dp[n-1][m-1])