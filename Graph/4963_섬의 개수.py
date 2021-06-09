# 연결되어 있는 노드 묶음 개수 세기 _ DFS

import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x<0 or x>n-1 or y<0 or y>m-1:
        return False

    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y]==1:
        graph[x][y]=0

        # 다른 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x-1, y-1)
        dfs(x-1, y+1)
        dfs(x+1, y-1)
        dfs(x+1, y+1)
        return True

    return False


while True:
    m, n = map(int, input().split())

    if n==0 and m==0:
        break

    graph=[]
    for i in range(n):
        graph.append(list(map(int, input().split())))


    result = 0
    for i in range(n):
        for j in range(m):
            #현재 위치에서 DFS수행
            if dfs(i, j) == True:
                result += 1

    print(result)

'''
https://www.acmicpc.net/problem/4963

입력예시
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0

출력
0
1
1
3
1
9
'''