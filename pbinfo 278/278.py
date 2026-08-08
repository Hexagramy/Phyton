n=int(input())
linie=input().split()
a=list()
for i in range(0,n):
    a.append(int(linie[i]))
m=int(input())
linie=input().split()
b=list()
for i in range(0,m):
    b.append(int(linie[i]))
maxim=max(b)
rez=0
for nr in a:
    if nr>maxim:
        rez+=1
print(rez)
