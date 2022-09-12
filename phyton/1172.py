vetor=[]

while len(vetor) <= 9:
    x = int(input())
    if x <=0:
        x = 1
    vetor.append(x)
    
for i in range(len(vetor)):
    print("X[{}] = {}".format(i,vetor[i]))