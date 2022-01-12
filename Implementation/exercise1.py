N=int(input())
arr=list(map(str,input().split()))
x,y=1,1


dx=[0,0,1,-1]
dy=[1,-1,0,0]
move=["R","L","D","U"]
for i in range(len(arr)):
    for j in range(len(move)):
        if arr[i]==move[j]:
            nx=x+dx[j]
            ny=y+dy[j]

    if nx<1 or ny<1 or nx>N or ny>N:
        continue
    else:
        x=nx
        y=ny

print(x,y)

