from collections import deque

n=int(input())
graph=[]

max_value=0
for i in range(n):
    graph.append(list(map(int, input().split())))
    max_value=max(max_value, max(graph[i]))


dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs(x, y, index, level):
    q=deque()
    q.append((x, y))

    while q:
        x, y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n and graph[nx][ny]>level and data[nx][ny]==-1:
                q.append((nx, ny))
                data[nx][ny]=index


result=1    #아무 지역도 물에 안잠길 수 있다

# 최대 높이까지만 수위 검사를 해주면 된다.
for level in range(max_value):
    data=[[-1] * n for _ in range(n)]   # 안전 영역 번호 매겨 넣을 2차원 배열
    index=0

    for i in range(n):
        for j in range(n):
            if graph[i][j]>level and data[i][j]==-1:
                bfs(i, j, index, level)
                index+=1
            
    result=max(result, index)   
    

print(result)