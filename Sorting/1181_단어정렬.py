import sys
data=set()

n=int(input())
for _ in range(n):
    k=sys.stdin.readline().rstrip()
    data.append((len(k), k))

data.sort(key=lambda x:(x[0], x[1]))

word=''
for datum in data:
    if datum!=word:
        print(datum[1])

    word=datum


'''
https://www.acmicpc.net/problem/1181

입력 예시
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours

출력
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
'''