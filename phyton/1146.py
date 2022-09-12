n = 1
lista = []
while n != 0:
    n = int(input())
    for x in range(1, n+1):
        lista.append(x)
    for i in range(n):
        if i == n-1:
            print(lista[i], end="\n")
            lista.clear()    
        else:
            print(lista[i] , end=" ")