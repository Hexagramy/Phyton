fin=open("arhitectura2.in","r")
fout=open("arhitectura2.out","w")
line=fin.readline()
n=int(line)
a=list(map(int,fin.readline().split()))
a.sort(reverse=True)
for i in a:
    fout.write(str(i))
    fout.write(" ")
fout.write('\n')
for i in range(0,n):
    if i==0:
        if a[0]==a[1]//2:
            fout.write(str(1))
            fout.write(" ")
        else:
            fout.write(str(0))
            fout.write(" ")
    else:
        if i==n-1:
            if a[n-1]==a[n-2]//2:
                fout.write(str(1))
                fout.write(" ")
            else:
                fout.write(str(0))
                fout.write(" ")
        else:
            if a[i]==(a[i-1]+a[i+1])//2:
                fout.write(str(1))
                fout.write(" ")
            else:
                fout.write(str(0))
                fout.write(" ")
    
fin.close()
fout.close()
