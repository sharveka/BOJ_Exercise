#다익스트라

import heapq, sys
input=sys.stdin.readline
INF=int(1e9)

#도시 개수 n, 버스 개수 m
n=int(input())
m=int(input())

#각 도시에서 버스로 갈 수 있는 도시에 대한 정보를 담는 리스트
graph=[[] for _ in range(n+1)]
#최단 거리 테이블 무한으로 초기화
distance=[INF]*(n+1)


#버스 정보 입력받기
for _ in range(m):
    a,b,c=map(int, input().split())
    graph[a].append((b,c))    #a도시에서 b도시로 가는 버스 비용 c

#출발 도시, 도착 도시
start, end=map(int, input().split())

def dijkstra(start):
    q=[]
    heapq.heappush(q, (0,start))
    distance[start]=0

    while q:
        dist, now=heapq.heappop(q)

        if distance[now]<dist:
            continue

        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

print(distance[end])


'''
https://www.acmicpc.net/problem/1916

입력 예시
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5

출력
4
'''