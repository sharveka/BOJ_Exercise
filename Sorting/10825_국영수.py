import sys 
input = sys.stdin.readline

#학생 수
n=int(input())
students=[]

for _ in range(n):
    students.append(input().split())

'''
1. 두 번째 원소 기준 내림차순
2. 두 번째 원소가 같으면, 세 번째 원소 기준 오름차순
3. 세 번째 원소가 같으면, 네 번째 원소 기준 내림차순
2. 네 번째 원소가 같으면, 첫 번째 원소 기준 오름차순
'''

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])

    
'''
https://www.acmicpc.net/problem/10825

입력 예시
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90

출력
Donghyuk
Sangkeun
Sunyoung
nsj
Wonseob
Sanghyun
Sei
Kangsoo
Haebin
Junkyu
Soong
Taewhan
'''