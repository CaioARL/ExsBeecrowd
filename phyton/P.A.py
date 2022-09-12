x = 1
v = int(input("Valor inicial:"))
r = int(input("Razão:"))
x = int(input("qtde termos"))
n = []*x

for x in range(x):
    n[x] = v + (x * r)
    x += 1
    continue
    
print(n)