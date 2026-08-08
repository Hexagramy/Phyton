n=int(input())
a=input().split()
ok=1
for i in range(0,n//2):
    if a[i]!=a[n-i-1]:
        ok=0
for i in range(0,n):
    print(str(a[i]),end="")
print()
if ok==1:
    print("DA")
else:
    print("NU")