n=int(input())
result=0

while n>0:
    if n%5==0:
        result+=(n//5)
        n=n%5

    else:
        n-=3
        result+=1

if n<0:
    print(-1)

else:
    print(result)
<<<<<<< HEAD


'''
https://www.acmicpc.net/problem/2839
입력 예시
18
출력
4
입력 예시
4
출력
-1
'''
=======
    
'''
https://www.acmicpc.net/problem/2839

입력 예시
18

출력
4

입력 예시
4

출력
-1
'''
>>>>>>> da3f00795e10ecfa1f3abe973555e9f028c6447e
