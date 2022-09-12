par =0
impar = 0
positivo = 0
negativo = 0

for x in range(1,6):
    a = int(input())
    if a % 2 ==0:
        par +=1

    if a % 2 != 0:
        impar +=1

    if a < 0:
        negativo +=1

    if a > 0:
        positivo +=1
print("{} valor(es) par(es)".format(par))
print("{} valor(es) impar(es)".format(impar))
print("{} valor(es) positivo(s)".format(positivo))
print("{} valor(es) negativo(s)".format(negativo))