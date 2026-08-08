from dataclasses import dataclass
@dataclass
class pereche:
    x:int
    nr:int
fin=open("frecventa1.in","r")
fout=open("frecventa1.out","w")
date=fin.read().split()
n=int(date[0]) 
v=list()
for i in range(0,101):
    p=pereche(i,0)
    v.append(p)
a=list(map(int,date[1:]))
for i in a:
    v[i].nr+=1
v.sort(key=lambda p:(-p.nr,p.x))
for i in v:
    if i.nr!=0:
        fout.write(str(i.x))
        fout.write(" ")
fin.close()
fout.close()