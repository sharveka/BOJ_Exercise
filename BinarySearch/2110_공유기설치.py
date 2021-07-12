# 거리로 이분탐색

import sys
input=sys.stdin.readline

n, c=map(int, input().split())

array=[]
for _ in range(n):
    array.append(int(input()))

array.sort()

# 가능한 최소거리와 최대거리
start=1 
end=array[-1]- array[0]
result=0

while start<=end:

    mid=(start+end)//2  # mid : 공유기 사이의 거리
    value=array[0]      # 맨 처음 위치에는 공유기를 설치해야 한다.
    count=1

    # 현재의 mid값을 이용해 mid 만큼 떨어진 거리에다 공유기 설치
    for i in range(1, n):
        if array[i]>=value+mid:
            value=array[i]
            count+=1

    if count>=c:        # C개 이상 설치할 수 있는 경우, 공유기 사이 거리를 넓혀보자
        start=mid+1
        result=mid      # 결과 저장

    else:               # 공유기를 C개보다 적게 설치한 경우 -> 공유기 사이 거리를 좁혀서 더 많이 설치해보자
        end=mid-1       

print(result)


'''
https://www.acmicpc.net/problem/2110

입력 예시
5 3
1
2
8
4
9

출력
3
'''