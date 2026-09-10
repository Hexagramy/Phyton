fin=open("eratostene.in",'r')
fout=open("eratostene.out",'w')
date=fin.read().split()
n=int(date[0])
a=[1]*1000005
a[0]=a[1]=0
for i in range(2,1000001):
    if a[i]==1:
        j=2
        while(i*j<=1000000):
            a[i*j]=0
            j+=1
rez=0
for i in range(0,n):
    nr=int(date[i+1])
    if a[nr]==1:
        rez+=1
fout.write(str(rez))
fin.close()
fout.close()