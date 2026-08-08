n=int(input())
a=list(map(int,input().strip().split()))
nr=int(a[0])
ogl=0
while nr>0:
    ogl=ogl*10+nr%10
    nr=nr//10
gasit=0
for i in range(1,n):
    if a[i]==ogl:
        gasit=1
if gasit==1:
    print("DA")
else:
    print("NU")