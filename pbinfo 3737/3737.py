import sys
date=sys.stdin.read().split()
n=int(date[0])
a=date[1:n+1]
m=dict()
nr=0
maxim=-1
st=dr=1
for i in a:
    nr+=1
    if i not in m:
        m[i]=nr
    else:
        if nr-m[i]>maxim:
            maxim=nr-m[i]
            st=m[i]
            dr=nr
print(st,dr)
