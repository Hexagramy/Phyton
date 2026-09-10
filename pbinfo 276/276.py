fin=open("pareimpare.in",'r')
fout=open("pareimpare.out",'w')
date=fin.read().split()
v=[0]*102
for i in date:
    nr=int(i)
    v[nr]=1
for i in range(0,101):
    if i%2==1:
        if v[i]==1:
            fout.write(str(i))
            fout.write(" ")
fout.write('\n')
for i in range(100,-1,-1):
    if i%2==0:
        if v[i]==1:
            fout.write(str(i))
            fout.write(" ")
fin.close()
fout.close()