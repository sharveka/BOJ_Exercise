import sys
from collections import deque
input=sys.stdin.readline

# 맵 크기, 바이러스의 종류
n,k=map(int, input().split())
# 맵 정보 담기
graph=[]
# 바이러스 정보 담기
virus_data=[]


for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j]!=0:  #바이러스면 정보를 담아주기
            virus_data.append((graph[i][j], 0, i,j))    #바이러스 종류, 시간, 위치

# 바이러스 종류 기준 오름차순 정렬 후 큐로 만들어주기
virus_data.sort()
q = deque(virus_data)

target_s, target_x, target_y=map(int, input().split())

dx=[-1,1,0,0]
dy=[0,0,-1,1]

while q:
    virus, s, x,y=q.popleft()

    # s초 지나거나 큐가 비면 중지
    if s==target_s:
        break

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx>-1 and ny>-1 and nx<n and ny<n:
            if graph[nx][ny]==0:
                graph[nx][ny]=virus
                q.append((virus, s+1, nx, ny))


print(graph[target_x-1][target_y-1])

'''
https://www.acmicpc.net/problem/18405

입력 예시
4 2
1 0 0 0
0 0 0 0
0 0 0 0
0 0 0 2
3 3 2

출력
1
'''