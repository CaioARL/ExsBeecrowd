x = int(input())
z = int(input())
soma = 0

while(z<=x):
    z = int(input())

for i in range(1,z):
    soma+=x
    x+=1
    if(soma > z):
        break
    else: 
        continue
print(i)
