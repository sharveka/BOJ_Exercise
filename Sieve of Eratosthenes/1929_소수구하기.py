import math

n=int(input())
data=list(map(int, input().split()))
big=max(data)

array=[True for _ in range(big+1)]
array[0], array[1]=False, False

for i in range(2, int(math.sqrt(big))+1):
    if array[i]==True:       #i가 소수인 경우
        #i를 제외한 i의 모든 배수를 지우기
        j=2
        while i*j<=big:
            array[i*j]=False
            j+=1


cnt=0
for datum in data:
    if array[datum]==True:
        cnt+=1

print(cnt)


'''
https://www.acmicpc.net/problem/1978

입력 예시
9
1 2 4 8 6 10 5 11 3

출력
4
'''