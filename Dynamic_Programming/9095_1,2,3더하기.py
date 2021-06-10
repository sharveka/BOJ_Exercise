# 다이나믹 프로그래밍 Bottom up

#테스트 케이스 개수 입력받기
case=int(input())

#각각의 케이스 입력받기
array=[]
for _ in range(case):
    array.append(int(input()))


# 먼저 구해진 결과 기록을 위한 DP테이블 초기화
d=[0]*(max(array)+1)
d[0]=1  
d[1]=1
d[2]=2

#bottom up programming
for num in array:
    for i in range(3, num+1):
        d[i]=d[i-3]+d[i-2]+d[i-1]

    print(d[num])


#d[4] 까지 직접 종이에 적어보면, d[i]=d[i-3]+d[i-2]+d[i-1] 와 같은 점화식을 도출할 수 있다.
'''
https://www.acmicpc.net/problem/9095

입력 예시
3
4
7
10

출력
7
44
274
'''