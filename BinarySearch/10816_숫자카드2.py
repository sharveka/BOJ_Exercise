from bisect import bisect_left, bisect_right
import sys
input=sys.stdin.readline


# 값이 [left_value, right_value] 인 데이터 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index=bisect_right(a, right_value)
    left_index=bisect_left(a, left_value)

    return right_index-left_index


n=int(input())
having=list(map(int, input().split()))
having.sort()

m=int(input())
x=list(map(int, input().split()))



for i in x:
    res=count_by_range(having, i, i)
    print(res, end=' ')