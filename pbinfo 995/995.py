fin=open("numere6.in","r")
fout=open("numere6.out","w")
line=fin.readline().split()
a=line[0]
b=line[1]
v=[0]*11
for c in a:
    v[int(c)]+=1
for c in b:
    v[int(c)]+=1
for i in range(9,-1,-1):
    for j in range(0,v[i]):
        fout.write(str(i))
fin.close()
fout.close()