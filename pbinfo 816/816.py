date=input().split()
n=int(date[0])
m=int(date[1])
if m%n==0:
    print(m//n)
else:
    print(m//n+1)