import sys
input=sys.stdin.readline

for tc in range(int(input())):
    cnt=1   #서류 1등은 일단 뽑힌다
    num=int(input())

    people=[]
    for _ in range(num):
        resume, interview=map(int, input().split())
        people.append((resume, interview))


    people.sort()       #서류 기준 오름차순 정렬
    max_interview=people[0][1]

    for i in range(1, num):
        #  다음 사람의 인터뷰 순위가 더 높아야 뽑힌다
        if max_interview>people[i][1]:
            cnt+=1
            max_interview=people[i][1]


    print(cnt)

