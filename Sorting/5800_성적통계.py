# 문제 조건을 똑바로 읽자

import sys
input=sys.stdin.readline

for i in range(int(input())):
    data=list(map(int, input().split()))
    data=data[1:]

    data.sort(reverse=True)

    largest_gap=0
    for j in range(len(data)-1):
        gap=data[j]-data[j+1]
        
        if gap>largest_gap:
            largest_gap=gap

    print(f"Class {i+1}")
    print(f"Max {data[0]}, Min {data[len(data)-1]}, Largest gap {largest_gap}")


'''
https://www.acmicpc.net/problem/5800

입력 예시
2
5 30 25 76 23 78
6 25 50 70 99 70 90

출력
Class 1
Max 78, Min 23, Largest gap 46
Class 2
Max 99, Min 25, Largest gap 25
'''