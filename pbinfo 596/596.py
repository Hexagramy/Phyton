fin=open("numere2.in","r")
fout=open("numere2.out","w")
line=fin.readline()
n=int(line)
line=fin.readline().split()
nr=0
a=list()
for i in line:
    x=int(i)
    if len(a)==0:
        a.append(x)
    else:
        l=len(a)
        if a[l-1]==x:
            nr+=1
            a.pop()
        else:
            a.append(x)
fout.write(str(nr))
fout.write('\n')
for i in a:
    fout.write(str(i))
    fout.write(" ")
fin.close()
fout.close()