import heapq

n=int(input())

#힙에 카드 묶음 넣기
heap=[]
for _ in range(n):
    data=int(input())
    heapq.heappush(heap,data)

result=0

#힙에 원소가 1개 남을때까지
while len(heap)!=1:
    #가장 작은 2개의 카드 묶음 꺼내기
    one=heapq.heappop(heap)
    two=heapq.heappop(heap)

    #카드 묶음을 합쳐서 다시 삽입
    sum_value=one+two
    result+=sum_value
    heapq.heappush(heap,sum_value)

print(result)


'''
https://www.acmicpc.net/problem/1715
입력 예시
3
10
20
40

출력
100
'''