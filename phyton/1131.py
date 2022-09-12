grenais,gremio,inter,empate = 0,0,0,0
venceu = ""
n=1

while n==1:
    a, b = list(map(int, input().split(" ")))
    grenais+=1
    print("Novo grenal (1-sim 2-nao)")
    n=int(input())
    if a>b:
        inter+=1
    if a<b:
        gremio+=1
    if a==b:
        empate+=1
if inter>gremio:
    venceu="Inter venceu mais"
if inter<gremio:
    venceu="Gremio venceu mais"

print("{} grenais".format(grenais))
print("Inter:{}".format(inter))
print("Gremio:{}".format(gremio))
print("Empates:{}".format(empate))
print(venceu)