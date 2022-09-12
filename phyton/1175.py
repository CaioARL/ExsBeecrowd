vetor=[]

for i  in range(20):
    e = int(input())
    vetor.append(e)

a = vetor[::-1]    

for j in range(20):
    print("N[{}] = {}".format(j,a[j]))