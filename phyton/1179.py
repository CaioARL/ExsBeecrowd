vPar = []
vImpar = []
ent = 0

while ent <=14:
    n = int(input())
    if n%2==0:
        vPar.append(n)
    else:
        vImpar.append(n)
        
    if len(vPar)==5:
        for x in range(5):
            print("par[{}] = {}".format(x, vPar[x]))
        vPar.clear()
    if len(vImpar)==5:
        for x in range(5):
            print("impar[{}] = {}".format(x, vImpar[x]))
        vImpar.clear()
    ent+=1
    
for x in range(len(vImpar)):
    print("impar[{}] = {}".format(x, vImpar[x]))
for x in range(len(vPar)):
    print("par[{}] = {}".format(x, vPar[x]))
