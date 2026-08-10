import sys
date=sys.stdin.read().split()
n=int(date[0])
m=int(date[1])
c=0
if date[2]=='+':
    c=1
v=list(map(int,date[3:]))
if c==0:
    v.sort(reverse=True)
else:
    v.sort()
a=list()
for i in range(0,n):
    linie=list()
    for j in range(0,m):
        linie.append(v[i*m+j])
    a.append(linie)
for i in range(0,n):
    for j in range(0,m):
        print(a[i][j],end=" ")
    print()
