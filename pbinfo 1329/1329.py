n=int(input())
a=list(map(int,input().split()))
ok=1
for i in range(0,n-2):
    if a[i]==a[i+1] or a[i+1]==a[i+2]:
        ok=0
    if a[i]<a[i+1] and a[i+1]<a[i+2]:
        ok=0
    if a[i]>a[i+1] and a[i+1]>a[i+2]:
        ok=0
if ok==1:
    print("DA")
else:
    print("NU")