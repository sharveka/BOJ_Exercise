#참고 : https://hazung.tistory.com/116

data=input()
count=1     #처음 숫자 세기

for i in range(len(data)-1):
    # 처음 숫자는 고려X , 뒤에 다른 숫자가 나오면 
    if data[i]!=data[i+1]:
        count+=1

print(count//2)


'''
https://www.acmicpc.net/problem/1439

입력예시
0001100

출력
1

'''