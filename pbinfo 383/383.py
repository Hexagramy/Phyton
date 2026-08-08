linie=input().split()
k=int(linie[0])
n=int(linie[1])
linie=input().split()
a=list()
for nr in linie:
    nr=int(nr)
    if nr%k>k//2:
        while nr%k!=0:
            nr+=1
    else:
        while nr%k!=0:
            nr-=1
    a.append(nr)
for i in range(n-1,-1,-1):
    print(a[i],end=" ")
