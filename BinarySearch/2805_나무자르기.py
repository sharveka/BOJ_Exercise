# 파라메트릭 서치 (Parametric Search) 
# 범위내에서 조건을 만족하는 가장 큰 값 찾기

import sys

n,m=map(int, sys.stdin.readline().split())
array=list(map(int, sys.stdin.readline().split()))

#시작점은 0, 끝점은 나무의 최대 길이로 설정 -> 안에서 이진탐색
start=0
end=max(array)

result=0

while start<=end:
    total=0     # 자른 나무값 총합
    mid=(start+end)//2

    # for x in array:
    #     # 나무 길이가 중간값(자르려는 위치)보다 크다면
    #     if x>mid:
    #         total+=x-mid    # 잘린 길이를 total에 더해주기
    
    #요렇게 하면 Pypy로 안해도 시간초과 안난다
    total=sum([x-mid for x in array if mid<x])  

    #다 잘랐는데 필요한 양보다 적다
    if total<m:
        end=mid-1       #좀 더 아래쪽에서 자른다

    #다 잘랐는데 필요한 양보다 많거나 같다
    else:
        result=mid      #최대한 덜 잘랐을 때가 정답이므로, 여기서 result에 값을 넣어주고 지나간다.
        start=mid+1     #좀 더 위쪽에서 자른다

        
print(result)



'''
https://www.acmicpc.net/problem/2805

입력 예시
4 7
20 15 10 17

출력
15
'''