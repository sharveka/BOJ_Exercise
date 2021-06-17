# 문자열 잘라서 정수형으로 변환
# 점수 입력하기
n=input()
left, right=0, 0

for i in range(len(n)):
    if i<(len(n)//2):
        left+=int(n[i])

    else:
        right+=int(n[i])

if left==right:
    print("LUCKY")

else:
    print("READY")


'''
https://www.acmicpc.net/problem/18406

입력 예시
123402

출력 
LUCKY

'''