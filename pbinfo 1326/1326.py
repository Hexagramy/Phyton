n=int(input())
a=input().split()
ok=1
i=0
while i+1<n and int(a[i])>int(a[i+1]):
    i+=1
if i==0 or i==n-1:
    ok=0
while i+1<n and int(a[i])<int(a[i+1]):
    i+=1
if i!=n-1:
    ok=0
if ok==1:
    print("DA")
else:
    print("NU")