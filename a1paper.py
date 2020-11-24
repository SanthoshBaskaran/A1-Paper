total_size=int(input())
a=list(map(int,input().split()))
list2=[0.594603557501, 0.420448207626]
do=total_size-3
s=0
r=1
count=0
for d in range(do):
    x=list2[s]
    y=list2[r]
    count=count+1
    if(d%2==0):
        p=x/2
        list2.append(p)
    elif(d%2!=0):
        q=y/2
        list2.append(q)
    if(count==2):
        s=s+2
        r=r+2
        count=0
tape=0.594603557501
for j in reversed(a):
    index1=a.index(j)
    index2=index1-1
    if(j>1):
        j=j//2
        f=list2[index1]*j
        tape=tape+f
        a[index2]+=j
        a[index1]=0
    if(a[0]==2):
        break
if(a[0]>=2):
    print(tape)
else:
    print('impossible')
