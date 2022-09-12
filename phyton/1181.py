linhaConta = int(input())
operacao = str(input())

matriz = []
for x in range(12):
    matriz.append([])
    
for posicao in range(12):
    for y in range(12):
        x = float(input())
        matriz[posicao].append(x)

if operacao == 'S':
    soma = 0
    for z in matriz[linhaConta]:
        soma += z
    print(soma)

if operacao == 'M':
    soma = 0
    for i in matriz[linhaConta]:
        soma += i
    print((soma/12))