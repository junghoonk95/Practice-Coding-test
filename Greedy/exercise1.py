N,M,K= map(int,input().split())
arr=list(map(int,input().split()))

arr=sorted(arr,reverse=True)

key=[]
for i in range(K):
    key.append(arr[0])

key.append(arr[1])

print(key)
key=key*M
ans=[]
for i in range(M):
    ans.append(key[i])

print(sum(ans))
