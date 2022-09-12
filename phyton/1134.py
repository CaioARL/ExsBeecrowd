a = int(input())
alc=0
gas=0
die=0

while a!=4:
    a = int(input())
    if a ==1:
        alc+=1
    elif a==2:
        gas+=1
    elif a==3:
        die+=1

print("MUITO OBRIGADO")
print("Alcool:",alc)
print("Gasolina:",gas)
print("Diesel:",die)