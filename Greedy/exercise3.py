N,K=map(int,input().split())

c=0

while N>1:
    if N%K==0:
        N=N//K
        c=c+1
    else:
        N=N-1
        c=c+1
print(c)
