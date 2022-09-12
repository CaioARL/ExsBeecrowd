y = int(input())
D = ["Brasilia", "Salvador", "Sao Paulo", "Rio de Janeiro", "Juiz de Fora", "Campinas", "Vitoria", "Belo Horizonte"]
ddd = [61, 71, 11, 21, 32, 19, 27, 31]

for x in range(len(ddd)):
    if y == int(ddd[x]):
        print(D[x])

if y!= 61 and y!= 71 and y!= 11 and y!= 21 and y!= 32 and y!= 19 and y!= 27 and y!= 31:
    print("DDD nao cadastrado")