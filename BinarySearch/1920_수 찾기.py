#1. 집합으로 풀기 
n=int(input())
array=set(map(int, input().split()))

m=int(input())
x=list(map(int, input().split()))

for i in x:
    if i in array:
        print(1)
    else:
        print(0)

'''
#2. 이진 탐색으로 풀기

def binary_search(array,target,start, end):
    while start<=end:
        mid=(start+end)//2

        #찾은 경우 중간점 인덱스 반환
        if array[mid]==target:
            return mid
        #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid]>target:
            end=mid-1
        #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start=mid+1

    return None

n=int(input())
array=list(map(int, input().split()))
array.sort()    #이진 탐색 수행 전 정렬 수행해두기

m=int(input())
x=list(map(int, input().split()))

for i in x:
    #해당 숫자가 존재하는지 확인
    result=binary_search(array, i, 0, n-1)

    if result!=None:
        print(1)
    else:
        print(0)

'''