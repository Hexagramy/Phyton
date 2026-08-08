n=int(input())
a=list()
linie=input().split()
for i in linie:
    a.append(int(i))
m=input()
b=list()
linie=input().split()
for i in linie:
    b.append(int(i))
b.sort()
gasit=0
for i in a:
    if i<b[0]:
        print(i,end=" ")
        gasit=1
if gasit==0:
    print("NU EXISTA")