import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(input()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]



def solution(x, y, index):
    q=deque()
    q.append((x, y))
    region[x][y]=index

    while q:
        x, y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n and region[nx][ny]==-1:
                if graph[nx][ny]==graph[x][y]:
                    q.append((nx,ny))
                    region[nx][ny]=index



region=[[-1] * n for _ in range(n)]
index=0
for i in range(n):
    for j in range(n):
        if region[i][j]==-1:
            solution(i,j, index)
            index+=1
print(index, end=' ')

for i in range(n):
    for j in range(n):
        if graph[i][j]=='G':
            graph[i][j]='R'


region=[[-1] * n for _ in range(n)]
index=0
for i in range(n):
    for j in range(n):
        if region[i][j]==-1:
            solution(i,j, index)
            index+=1
print(index)