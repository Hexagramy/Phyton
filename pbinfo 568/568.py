import sys
date=sys.stdin.read().split()
n=int(date[0])
m=int(date[1])
v=list(map(int,date[2:]))
a=list()
for i in range(0,n):
    linie=list()
    for j in range(0,m):
        linie.append(v[i*m+j])
    a.append(linie)
rez=0
for j in range(0,m):
    minim=10002
    for i in range(0,n):
        minim=min(minim,a[i][j])
    rez+=minim
print(rez)
    