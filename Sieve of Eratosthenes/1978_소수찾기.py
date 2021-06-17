import math

n,m=map(int, input().split())


array=[True for _ in range(m+1)]
array[1]=False

for i in range(2, int(math.sqrt(m))+1):     #루트기준으로 좌우 대칭
    if array[i]==True:       #i가 소수인 경우
        #i를 제외한 i의 모든 배수를 지우기
        j=2
        while i*j<=m:
            array[i*j]=False
            j+=1


for i in range(n, m+1):
    if array[i]==True:
        print(i)

'''
https://www.acmicpc.net/problem/1929

입력 예시
3 16

출력
3
5
7
11
13
'''