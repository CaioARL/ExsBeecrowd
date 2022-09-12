n = int(input())
s = 0
for z in range(1,n+1):
    X,Y=list(map(int,input().split(" ")))
    s=0
    if X > Y:
        for a in range((Y+1),X):
            if (a%2) != 0:
                s+=a

    if X < Y:
        for b in range(X+1,Y):
            if (b%2) != 0:
                s+=b
                
    if X==Y:
        s = 0
    print(s)