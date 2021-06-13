#다익스트라 알고리즘 - 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램. 

import heapq,sys
input=sys.stdin.readline
INF=int(1e8)        #무한을 의미하는 자연수로 1억을 설정

#정점의 개수 V, 간선의 개수 E 입력
v, e=map(int, input().split())
#시작 정점의 번호
start=int(input())

#각 도시의 연결 정보를 담을 리스트 만들기
graph=[[] for _ in range(v+1)]  #정점은 1번부터 시작한다.
#최단 거리 테이블을 무한으로 초기화
distance=[INF]*(v+1)

#모든 간선 정보 입력받기
for _ in range(e):
    a,b,c=map(int, input().split())
    #a번 노드에서 b번 노드로 가는 간선의 가중치 c
    graph[a].append((b,c))


def dijkstra(start):
    q=[]

    #시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
    heapq.heappush(q, (0,start))
    distance[start]=0

    #큐가 빌 때까지 반복
    while q:
        #최단거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now=heapq.heappop(q)

        #해당 도시를 방문한 적 있고, 그 거리가 최단거리라면 건너뛰기
        if distance[now]<dist:
            continue

        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:        #graph[now]에는 (b,c) - now에서 b로 가는 비용 c가 들어있다.
            cost=dist+i[1]

            #현재 노드를 거쳐서 b로 가는 거리가 더 짧은 경우 -> 최단 거리 갱신
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, v+1):
    if distance[i]==INF:
        print("INF")

    else:
        print(distance[i])





'''
https://www.acmicpc.net/problem/1753

입력 예시
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

출력
0
2
3
7
INF
'''