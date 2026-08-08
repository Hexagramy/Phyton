import sys
date=sys.stdin.read().split()
n=int(date[0])
a=[0]*102
ok=1
for i in range(1,n+1):
    if int(date[i])>n:
        ok=0
    else:
        a[int(date[i])]+=1
        if a[int(date[i])]>1:
            ok=0     
if ok==1:
    print("DA")
else:
    print("NU")