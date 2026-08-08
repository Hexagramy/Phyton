import sys
date=sys.stdin.read().split()
n=int(date[0])
a=list(map(int,date[1:]))
gasit=0
for i in range(1,n-1):
    ok=1
    if a[i]%2!=a[i+1]%2:
        ok=0
    if a[i]%2!=a[i-1]%2:
        ok=0
    if ok==1:
        gasit=1
if gasit==1:
    print("DA")
else:
    print("NU")
