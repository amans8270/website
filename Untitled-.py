t=int(input(""))
l=[]
count=0
def operation(l):
    diff=l[0]-l[1]
    while(l[0]!=l[1]):
        if(diff>0):
            if(diff%2==0):
                l[0]=l[0]-2
                count+=1
            else:
                n=diff//2
                count=n+1
    print(count)
for i in range(0,t):
    l=list(map(int,input("").strip().split()))
    count=0
    operation(l)

