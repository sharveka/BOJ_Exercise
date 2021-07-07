# BFS - 모든 도로의 비용이 1, 단방향
# 입력을 input으로만 하면 시간초과 난다. -> sys.stdin.readline

import sys
from collections import deque
input=sys.stdin.readline

# 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
n,m,k,x=map(int, input().split())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)

INF=int(1e9)
road=[INF]*(n+1)
road[x]=0

def bfs(x):
    queue=deque([x])

    while queue:
        current=queue.popleft()

        for i in graph[current]:
            if road[i]>road[current]+1:
                road[i]=road[current]+1
                queue.append(i)            


bfs(x)
cnt=0
for i in range(1, len(road)):
    if road[i]==k:
        print(i)
        cnt+=1

if cnt==0:
    print(-1)


'''
https://www.acmicpc.net/problem/18352

입력 예시
4 4 2 1
1 2
1 3
2 3
2 4

출력
4
'''