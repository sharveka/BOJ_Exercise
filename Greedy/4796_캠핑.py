case=1
while True:
    l, p, v = map(int, input().split())
    if l==0 and p==0 and v==0:
        break

    count1=(v//p)
    if v % p>l:
        count2=l
    else:
        count2= v%p

    result= count1*l + count2
    print(f"Case {case}: {result}")
    case+=1



'''
https://www.acmicpc.net/problem/4796

입력 예시
5 8 20
5 8 17
0 0 0

출력
Case 1: 14
Case 2: 11
'''