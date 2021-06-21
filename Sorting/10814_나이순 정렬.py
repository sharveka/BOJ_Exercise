import sys
input=sys.stdin.readline

n=int(input())
people=[]

for i in range(n):
    people.append((input().split()))

'''
1. 나이순 오름차순
2. 나이가 같으면 가입한 순(가입 순서는 입력 순서와 같다.)

입력 순서와 가입 순서가 같으므로, 2번에 대해서는 정렬할 필요 없다.
'''
people.sort(key=lambda x:(int(x[0])))

for person in people:
    print(person[0], person[1])



'''
https://www.acmicpc.net/problem/10814

입력 예시
3
21 Junkyu
21 Dohyun
20 Sunyoung

출력
20 Sunyoung
21 Junkyu
21 Dohyun
'''