n=int(input())
a=list(map(int, input().split()))
a.sort()

#중간값을 출력
print(a[(n-1)//2])


'''
https://www.acmicpc.net/problem/18310

입력 예시
4
5 1 7 9

출력
5

'''