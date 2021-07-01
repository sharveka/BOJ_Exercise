# 시뮬레이션

# 맵 크기, 사과의 개수
n=int(input())
k=int(input())  

data=[[0]*(n+1) for _ in range(n+1)]    # 맵 정보
info = []  # 방향 회전 정보


# 사과 위치 입력받기
for _ in range(k):
    a, b=map(int, input().split())
    data[a][b]=1


#방향 회전 정보
l = int(input())
for _ in range(l):
    x, c=input().split()
    info.append((int(x), c))        # x 초 후 회전


# 동, 남, 서, 북
dx=[0, 1, 0, -1]
dy=[1,0,-1, 0]

def turn(direction, c):
    if c=="L":
        direction=(direction-1)%4
    else:
        direction=(direction+1)%4

    return direction


def simulate():
    x, y=1, 1   # 시작 위치
    data[x][y]=2   # 뱀이 있는 위치는 2로 표시
    direction=0     # 처음에는 동쪽을 보고 있다

    time=0      # 시작한 뒤에 지난 시간(초)
    index=0     #다음에 회전할 정보

    q=[(x, y)]

    while True:
        nx=x+dx[direction]
        ny=y+dy[direction]

        # 맵 안에 있고, 뱀의 몸통이 없는 위치라면
        if nx>=1 and nx<=n and ny>=1 and ny<=n and data[nx][ny]!=2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny]==0:
                data[nx][ny]=2
                q.append((nx, ny))
                
                px, py=q.pop(0)
                data[px][py]=0

            if data[nx][ny]==1:
                data[nx][ny]=2
                q.append((nx, ny))

        # 맵의 벽과 부딪히거나 뱀의 몸통과 부딪혔다
        else:
            time+=1
            break

        x, y=nx, ny
        time+=1

        if index<l and time==info[index][0]:        #회전할 시간이다
            direction=turn(direction, info[index][1])
            index+=1

    return time


print(simulate())


'''
https://www.acmicpc.net/problem/3190

입력 예시
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L

출력
21
'''