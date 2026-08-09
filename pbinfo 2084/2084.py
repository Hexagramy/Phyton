import sys
date=sys.stdin.read().split()
n=int(date[0])
a=list(map(int,date[1:n+1]))
lmax=a[0]
rmax=a[n-1]
i=1
j=n-2
rez=0
while i<=j:
    if lmax<=rmax:
        rez+=max(0,lmax-a[i])
        lmax=max(lmax,a[i])
        i+=1
    else:
        rez+=max(0,rmax-a[j])
        rmax=max(rmax,a[j])
        j-=1
print(rez)