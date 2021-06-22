# 이진 탐색 코드
def binary_search(data, target, start, end):
    if start>end:
        return None

    mid=(start+end)//2

    if data[mid]==target:
        return True
    
    elif data[mid]>target:
        return binary_search(data, target, start, mid-1)

    else:
        return binary_search(data, target, mid+1, end)

n=int(input())
mine=list(map(int, input().split()))
mine.sort()     #이진 탐색은 정렬되어 있는 코드에서 동작한다.

m=int(input())
data=list(map(int, input().split()))

for a in data:
    if binary_search(mine, a, 0, n-1)==True:
        print(1, end=' ')
    
    else:
        print(0, end=' ')



# Set 자료형 활용 코드        
n=int(input())
mine=set(map(int, input().split()))

m=int(input())
data=list(map(int, input().split()))

for datum in data:
    if datum in mine:
        print(1, end=' ')
    else:
        print(0, end=' ')