N,M= map(int,input().split())

x,y,d=map(int,input().split())

arr=[list(map(int,input().split())) for _ in range(N)]


nx=[0,1,0,-1]
ny=[1,0,-1,0]
dir=[3,2,1,0]

count=1

def move(x,y):
    global count
    for i in range(4):
        dx = x + nx[dir[d - i]]
        dy = y + ny[dir[d - i]]
        if dx < 0 or dy < 0 or dx > M or dy > N or arr[dy][dx] == 1:
            continue

        else:
            x=dx
            y=dy
            arr[dy][dx]=1
            count=count+1
            move(x,y)

    return(count)
move(x,y)
print(count)


##오류 발견
