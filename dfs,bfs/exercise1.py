#음료수 얼려먹기

N,M= map(int,input().split())

arr=[list(map(int,input())) for _ in range(N)]
visit=arr
x,y=0,0

ny=[1,-1,0,0]
nx=[0,0,1,-1]
count=0
def go(y,x):
    global count, visit
    for i in range(4):
        dx=x+nx[i]
        dy=y+ny[i]

        if dx<0 or dy<0 or dy>=N or dx>=M or arr[dy][dx]==1:
            continue

        if visit[dy][dx]==0:
            visit[dy][dx]=1
            go(dy,dx)
    return visit

for i in range(N):
    for j in range(M):
        if visit[i][j]==0:
            visit[i][j]=1
            go(i,j)
            count=count+1

print(count)
