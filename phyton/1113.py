X,Y=list(map(int,input().split(" ")))

while X!=Y:
    if X > Y:
        print("Decrescente")
        X,Y=list(map(int,input().split(" ")))
        
    if X < Y:
        print("Crescente")   
        X,Y=list(map(int,input().split(" ")))