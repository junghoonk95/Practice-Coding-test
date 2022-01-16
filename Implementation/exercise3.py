N,M= map(int,input().split())

x,y,d=map(int,input().split())

arr=[list(map(int,input().split())) for _ in range(N)]
visit=arr

nx=[-1,0,1,0]
ny=[0,-1,0,1]


count=0
def play(x,y):
    global dy,dx, count
    for i in range(4):
        dy = y + ny[i]
        dx = x + nx[i]
        if dy<0 or dx<0 or dy>N or dx>M or arr[dy][dx]==1:
            continue
        else:
            if visit[dy][dx] == 0:
                visit[dy][dx] = 1
                x = dx
                y = dy
                count=count+1
                play(x,y)


for i in range(4):
    dx=x+nx[i]
    dy=y+ny[i]
    if dy < 0 or dx < 0 or dy > N or dx > M:
        continue
    else:
        play(x,y)

print(count)



