import sys
input=sys.stdin.readline

n=int(input())
data=[]
for _ in range(n):
    data.append(int(input()))

data.sort()

max_value=0
for i in range(n):
    x=data[i]*(n-i)
    max_value=max(x, max_value)

print(max_value)

'''
https://www.acmicpc.net/problem/2217

입력 예시
4
10
15
20
30

출력
45
'''