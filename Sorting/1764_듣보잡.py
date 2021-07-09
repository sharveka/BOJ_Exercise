# 정렬을 하면 중복되는 것은 항상 붙어있게 된다!
# 해당 문제의 입력은 중복이 최대 2개이기 때문에 가능

import sys
input=sys.stdin.readline

n,m=map(int, input().split())
data=[]
answer=[]

for _ in range(n+m):
    data.append(input().rstrip())
    
data.sort()

for i in range(n+m-1):
    if data[i]==data[i+1]:
        answer.append(data[i])


print(len(answer))
for name in answer:
    print(name)

'''
https://www.acmicpc.net/problem/1764

입력 예시
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton

출력
2
baesangwook
ohhenrie
'''