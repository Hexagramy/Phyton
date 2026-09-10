import sys
date=sys.stdin.read().split()
x=int(date[0])
n=int(date[1])
a=list(map(int,date[2:]))
st=0
dr=n
rez=-1
while st<dr:
    m=(st+dr)//2
    if a[m]==x:
        rez=m
        break
    else:
        if x<a[m]:
            dr=m
        else:
            st=m+1
if rez==-1:
    print("Nu exista")
else:
    print("Da",rez)