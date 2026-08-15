import sys
date=sys.stdin.read().split()
n=int(date[0])
m=int(date[1])
minim=1000000004
poz=0
a=list()
for i in range(0,n):
    linie=list()
    for j in range(0,m):
        linie.append(int(date[m*i+j+2]))
        if int(date[m*i+j+2])<minim:
            minim=int(date[m*i+j+2])
            poz=j
    a.append(linie)
for i in range(0,n):
    a[i][poz]=a[n-1][m-1]
for i in range(0,n):
    for j in range(0,m):
        print(a[i][j],end=" ")
    print()