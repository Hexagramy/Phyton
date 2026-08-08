import sys
date=sys.stdin.read().split()
n=int(date[0])
a=list(date[1:n])
m=int(date[n+1])
b=list(date[n+2:])
for i in b:
    if a.__contains__(i)==True:
        print("1",end=" ")
    else:
        print("0",end=" ")