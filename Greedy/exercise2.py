N,M=map(int,input().split())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))

minmum=0
for i in range(N):
    if min(arr[i])>minmum:
        minmum=min(arr[i])

print(minmum)
