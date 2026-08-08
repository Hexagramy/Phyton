n=int(input())
for i in range(2,n):
    if n%i==0:
        d1=i
        break
print(int(d1+n/d1))