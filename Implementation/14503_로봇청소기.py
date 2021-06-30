# 행 개수 n x 열 개수 m 맵
n,m=map(int, input().split())
# 처음 위치와 방향 입력
x, y, direction=map(int, input().split())
#북, 동, 남, 서 - 0, 1, 2, 3
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

#방문 정보를 담을 배열 - 0으로 초기화
d=[[0]*m for _ in range(n)]
d[x][y]=1   #첫번째 좌표는 방문 처리
data=[]
for i in range(n):
    data.append(list(map(int, input().split())))


def turn_left():
    global direction
    direction-=1

    if direction==-1:
        direction=3



count=1         # 청소한 곳 개수
turn_time=0     # 회전 횟수 

while True:
    # 왼쪽을 보자
    turn_left()
    nx=x+dx[direction]
    ny=y+dy[direction]

    # 해당 위치를 방문도 안했고 벽도 아니다
    if d[nx][ny]==0 and data[nx][ny]==0:
        x, y=nx, ny
        d[x][y]=1

        count+=1
        turn_time=0
        continue
    
    # 방문을 했거나 벽이다
    else:
        turn_time+=1

    # 다 돌아봤는데 청소할 곳이 없다
    if turn_time==4:
        # 뒤로 한번 가볼까
        nx=x-dx[direction]
        ny=y-dy[direction]

        # 뒤가 벽이라 후진이 안된다 
        if data[nx][ny]==1:
            break

        else:
            x, y=nx, ny
            
        turn_time=0

print(count)