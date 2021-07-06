#BFS

from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    # queue
    queue=deque()
    queue.append((x, y))

    while queue:
        x, y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            # 미로 범위를 벗어나거나 벽인 경우
            if nx<0 or ny<0 or nx>n-1 or ny>m-1 or graph[nx][ny]==0:
                continue

            # 처음 방문한다
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx, ny))
    
    return graph[n-1][m-1]


print(bfs(0,0))

'''
https://www.acmicpc.net/problem/2178

입력 예시
4 6
101111
101010
101011
111011

출력
15

'''