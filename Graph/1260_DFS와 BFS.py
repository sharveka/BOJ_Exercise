#DFS, BFS 기본 - 간선이 단방향일때와 양방향일때 입력에 주의하자

# 정점의 개수, 간선의 개수, 탐색 시작 노드
import sys
from  collections import deque
input=sys.stdin.readline
n,m,v=map(int, input().split())

# 간선 연결 정보를 받을 2차원 리스트 (*** 간선은 양방향이다!)
graph=[[] for _ in range(n+1) ]
for _ in range(m):
    a,b=map(int, input().split())
    # 양방향 간선일때는 두 번 다 넣어주어야 한다.
    graph[a].append(b)
    graph[b].append(a)

for x in graph:
    x.sort()

print(graph)

def dfs(graph, v, visited):
    visited[v]=True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    queue=deque([v])
    # 현재 노드를 방문 처리
    visited[v]=True

    while queue:
        v=queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True


visited=[False]*(n+1)
dfs(graph, v, visited)
print()
visited=[False]*(n+1)
bfs(graph, v ,visited)


'''
https://www.acmicpc.net/problem/1260

입력 예시
5 5 3
5 4
5 2
1 2
3 4
3 1
출력
3 1 2 5 4
3 1 4 2 5
'''