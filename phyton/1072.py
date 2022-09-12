n = int(input())

entrada = 0
saida = 0

for x in range(1, n+1):
    x = int(input())
    if x >= 10 and x <=20:
        entrada += 1
    else:
        saida +=1

print("{} in".format(entrada))
print("{} out".format(saida)) 