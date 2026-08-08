fin=open("secv_fb.in","r")
fout=open("secv_fb.out","w")
line=fin.readline().strip()
line=line.split()
n=int(line[0])
k=int(line[1])
line=fin.readline().strip().split()
a=list()
v=dict()
for i in range(0,n):
    a.append(int(line[i]))
    v[int(line[i])]+=1
