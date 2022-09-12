a,b=list(map(int,input().split(" ")))
lista = ""
soma=0

while (b>0) and (a>0):
    if a >b:
        for x in range(b,a+1):
            lista+= str(x) + " "
            soma+=x
        print("{}Sum={}".format(lista,soma))
        soma=0
        lista=""
    if a < b:
        for x in range(a,b+1):
            lista+= str(x) + " "
            soma+=x
        print("{}Sum={}".format(lista,soma))
        soma=0
        lista=""
    a,b=list(map(int,input().split(" ")))