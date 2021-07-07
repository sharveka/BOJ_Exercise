import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x,y):
    if x<0 or y<0 or x>n-1 or y>m-1:
        return False
    
    # 현재 노드를 아직 방문 안했다
    if farm[x][y]==1:
        farm[x][y]=2

        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False



for _ in range(int(input())):
    n,m,k=map(int, input().split())
    farm=[[0] * m for _ in range(n)]

    for _ in range(k):
        a,b=map(int,input().split())
        farm[a][b]=1

    result=0

    for x in range(n):
        for y in range(m):
            if dfs(x, y):
                result+=1
                                   
    print(result)

    


'''

https://www.acmicpc.net/problem/1012
입력 예시
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5

출력
5
1

'''