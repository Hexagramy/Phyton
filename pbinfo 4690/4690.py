import sys
date=sys.stdin.read().split()
n=int(date[0])
m=int(date[1])
a=list()
for i in range(0,n):
    linie=list()
    for j in range(0,m):
        linie.append(int(date[m*i+j+2]))
    a.append(linie)
nr=0
for i in range(0,n):
    for j in range(0,m):
        s=0
        if i-1>=0:
            s+=a[i-1][j]
        if i+1<n:
            s+=a[i+1][j]
        if j-1>=0:
            s+=a[i][j-1]
        if j+1<m:
            s+=a[i][j+1]
        if a[i][j]>s:
            nr+=1
print(nr)