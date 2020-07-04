n=int(input(""))
def player():
    t=int(input(""))
    p=[]
    q=[]
    l=[]
    m=[]
    l=list(map(int,input("").strip().split()))
    m=list(map(int,input("").strip().split()))
    m=sorted(m)
    l=sorted(l)
    count=0
    y=t-1
    u=0
    for i in range(t-1,0,-1):
        if(m[i]>l[y]):
            u+=1    
        else:
            count+=1
            y-=1
    print(count)
    print(u)
for i in range(0,n):
    player()
