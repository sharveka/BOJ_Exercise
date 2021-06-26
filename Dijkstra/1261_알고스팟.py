#다익스트라
#붙어있는 숫자 입력값 입력받기 

import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

# 상, 우, 하 , 좌
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

m,n =map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int, input().rstrip())))

#최단 거리 테이블 무한으로 초기화
distance=[[INF]*m for _ in range(n)]

# print(graph)
# for i in range(n):
#     for j in range(m):
#         print(graph[i][j], end=' ')
#     print()
# 시작 노드 처리

x, y=0,0
q=[(graph[x][y], x, y)]
distance[x][y]=graph[x][y]

#다익스트라 알고리즘 수행
while q:
    dist, x, y=heapq.heappop(q)

    if distance[x][y]<dist:
        continue

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        #맵을 벗어나면 무시
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue

        cost=dist+graph[nx][ny]

        if cost<distance[nx][ny]:
            distance[nx][ny]=cost
            heapq.heappush(q, (cost, nx, ny))

print(distance[n-1][m-1])