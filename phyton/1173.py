a = int(input())
vetor=[]

while a<=50:
    for x in range(10):
        vetor.append(a)
        print("N[{}] = {}".format(x,vetor[x])) 
        a*=2   