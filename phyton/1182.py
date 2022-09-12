coluna = int(input())
matriz=[]
operacao = str(input())

for i in range(12):
    matriz.append([])
    for x in range(12):
        num = float(input())
        matriz[i].append(num)
        
soma=0
        
for x in range(12):
    soma += matriz[x][coluna]
    
if operacao == 'S':
    print(f'{soma:.1f}')
elif operacao == 'M':
    soma = soma/12
    print(f'{soma:.1f}')