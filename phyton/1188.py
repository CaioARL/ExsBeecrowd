operacao = str(input())

matriz =[]

for i in range(12):
    matriz.append([])
    for x in range(12):
        num = float(input())
        matriz[i].append(num)

posi = [5,6]
soma = 0
x=0
for linha in range(7,12):
    inicial = 5 - x
    final = 6 + x
    for i in range(inicial, final+1):
        soma += matriz[linha][i]
    x+=1
    
if operacao =='S':
    print(f'{soma:.1f}')
elif operacao == 'M':
    soma = soma/30
    print(f'{soma:.1f}')