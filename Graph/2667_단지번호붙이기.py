# 연결되어 있는 노드 묶음 개수 세기 _ DFS

import sys
sys.setrecursionlimit(10**5)    #10^5


def dfs(x, y):
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x < 0 or x > size-1 or y < 0 or y > size-1:
        return False

    global cnt

    #현재 노드를 아직 방문하지 않았다면
    if array[x][y] == 1:
        #해당 노드 방문 처리
        array[x][y] = 2
        cnt+=1

        #상,하,좌,우 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True

    return False


size = int(input())
array=[]
for _ in range(size):
    array.append(list(map(int, input())))

result = 0
cnt_arr=[]
cnt=0

for i in range(size):
    for j in range(size):
        #현재 위치에서 DFS 수행
        if dfs(i, j):
            result += 1
            cnt_arr.append(cnt)
            cnt=0

print(result)

for i in sorted(cnt_arr):
    print(i)

'''
https://www.acmicpc.net/problem/2667

입력 예시
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

출력
3
7
8
9

'''

'''
Recursion Error 발생. 맨 위 두줄을 넣어주었더니 정답.
Python이 정한 최대 재귀 깊이보다 재귀의 깊이가 더 깊어질 때 발생.
sys.getrecursionlimit()을 이용해 확인 가능. BOJ의 채점 서버는 1000으로 되어있다.
visual code 는 백만으로 되어있다.
'''