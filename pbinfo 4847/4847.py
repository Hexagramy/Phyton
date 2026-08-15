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
for j in range(1,m-1):
    if a[0][j]==a[0][j-1]==a[0][j+1]==0:
        nr+=1
for j in range(1,m-1):
    if a[n-1][j]==a[n-1][j-1]==a[n-1][j+1]==0:
        nr+=1
print(nr)