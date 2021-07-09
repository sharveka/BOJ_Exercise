# set 자료형으로 만들어서 중복 제거 -> 리스트로 다시 돌려놓기

n=int(input())
data=list(map(int, input().split()))

d=list(set(data))
d.sort()
for i in d:
    print(i, end=' ')