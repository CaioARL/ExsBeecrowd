cont = int(input())

for x in range(cont):
    dados = list(map(str,input().split(' ')))
    if dados[0] == 'Thor':
        print('Y') 
    else:
        print('N')