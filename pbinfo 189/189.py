n=int(input())
a=input().split()
for i in range(0,n):
    v=list()
    nr=int(a[i])
    nr_cif=0
    while nr>0:
        v.append(nr%10)
        nr=nr//10
        nr_cif+=1
    nr=int(a[i])
    v.reverse()
    ok=1
    i=0
    while i+1<nr_cif and v[i]<v[i+1]:
        i=i+1
    if i==0 or i==nr_cif-1:
        ok=0
    while i+1<nr_cif and v[i]>v[i+1]:
        i=i+1
    if i!=nr_cif-1:
        ok=0
    print(ok)
    
