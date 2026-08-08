n=int(input())
gasit=0
for i in range(0,2000000000):
    x=i
    p=1
    while x>0:
        p=p*(x%10)
        x=int(x/10)
    if p==n:
        gasit=i
        break
print(gasit)
