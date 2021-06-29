# 그리디, 뒤에서부터 검사해야 한다.

n=int(input())
array=[]

for _ in range(n):
    array.append(int(input()))

result=0
for i in range(n-1, 0, -1):     #n-1 부터 0보다 큰 동안 -1씩 감소
    if array[i-1]>=array[i]:
        minus=array[i]-array[i-1]-1

        array[i-1]=array[i-1]+minus
        result-=minus



print(result)


'''
https://www.acmicpc.net/problem/2847
입력 예시
4
5 
6
7
6


출력
6


'''