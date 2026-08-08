n=int(input())
a=input().split()
v=list()
for i in a:
    v.append(int(i[0]))
v.sort()
for i in v:
    print(str(i),end="")