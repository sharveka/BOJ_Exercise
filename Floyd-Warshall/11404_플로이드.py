#플로이드 워셜

# 도시 개수 n, 버스 개수 m
n=int(input())
m=int(input())
INF=int(1e9)
# 인접행렬 만들기
graph=[[INF] * (n+1) for _ in range(n+1)]   #1번 도시부터 시작

#자기 자신으로 가는비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b]=0


#각 간선에 대한 정보를 입력받아 초기화
for _ in range(m):
    a, b, c=map(int, input().split())
    #a도시에서 b도시로 가는 비용 c
    graph[a][b]=min(graph[a][b], c)     #도시 간 중복 노선이 있다


#플로이드 워셜
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])


#결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b]==INF:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()


'''
https://www.acmicpc.net/problem/11404

입력예시
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4

출력
0 2 3 1 4
12 0 15 2 5
8 5 0 1 1
10 7 13 0 3
7 4 10 6 0
'''