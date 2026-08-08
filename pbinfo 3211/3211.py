date=input().split()
s=int(date[0])
c=int(date[1])
n=int(date[2])
ok1=1
ok2=1
if s%c!=0:
    ok1=0
if s%n!=0:
    ok2=0
if ok1==True and ok2==True:
    print("CN")
else:
    if ok1==True and ok2==False:
        print("C")
    else:
        if ok1==False and ok2==True:
            print("N")
        else:
            print("nimic")