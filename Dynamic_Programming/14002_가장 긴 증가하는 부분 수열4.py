n=int(input())
array=list(map(int, input().split()))

dp=[1]*(n+1)

for i in range(1, n):
    for j in range(0, i):
        if array[j]<array[i]:
            dp[i]=max(dp[i], dp[j]+1)

max_cnt=max(dp)
print(max_cnt)
max_index=dp.index(max(dp))

seq=[]
for i in range(max_index, -1, -1):
    if dp[i]==max_cnt:
        seq.append(array[i])
        max_cnt-=1

for x in seq[::-1]:
    print(x, end=' ')

