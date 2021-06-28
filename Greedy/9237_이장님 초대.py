# 오래 자라는 나무부터 심고, 인덱스+1 에 나무가 자라는 날짜를 더해준다. 이장님은 다 자란 다음날 방문
n=int(input())
data=list(map(int, input().split()))
data.sort(reverse=True)

max_value=0
for i in range(n):
    x=data[i]+i+1
    max_value=max(max_value, x)

print(max_value+1)


'''
for i in range(n):
    t[i]+=i
print(max(t)+2)
'''

'''
https://www.acmicpc.net/problem/9237

입력 예시
6
39 38 9 35 39 20

출력
42
'''