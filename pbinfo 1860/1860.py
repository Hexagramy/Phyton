f=open(r"C:\\Users\\Hexagramy\\Desktop\\Phyton\\pbinfo 1860\\blackfriday.in",'r')
o=open("blackfriday.out",'w')
n=int(f.readline())
s1 = list(map(int, f.readline().split()))
s2 = list(map(int, f.readline().split()))
maxim = (s1[0] - s2[0]) / s1[0] * 100
poz=0
for i in range(0,n):
    if (s1[i] - s2[i]) / s1[i] * 100>maxim:
        maxim=(s1[i] - s2[i]) / s1[i] * 100
        poz=i
o.write(str(poz+1))
#print(int(s2[0])/int(s1[0]))
f.close()
o.close()