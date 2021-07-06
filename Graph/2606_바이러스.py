import sys
from collections import deque

input=sys.stdin.readline
n=int(input())
m=int(input())

graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[False]*(n+1)

def bfs(v):
    # queue
    queue=deque([v])
    visited[v]=True
    cnt=0

    while queue:
        x=queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)
                cnt+=1

    return cnt


print(bfs(1))