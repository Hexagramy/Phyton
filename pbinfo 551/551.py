import sys
date=sys.stdin.read().split()
n=int(date[0])
m=int(date[1])
maxim=0
nr=0
for i in range(0,n):
    a=list(map(int,date[2+m*i:2+m*(i+1)]))
    for i in a:
        if i>maxim:
            maxim=i
            nr=0
    if a.__contains__(maxim):
            nr+=1
print(maxim,nr)