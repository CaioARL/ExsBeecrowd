n = int(input())
vetor=input()
vetor=vetor.split()

for i in range(len(vetor)):
    vetor[i]=int(vetor[i])

menor=vetor[0]
posicao=0

for x in range(1,len(vetor)):
    if vetor[x]<menor:
        menor=vetor[x]
        posicao=x
        
print("Menor valor: {}".format(menor))
print("Posicao: {}".format(posicao))