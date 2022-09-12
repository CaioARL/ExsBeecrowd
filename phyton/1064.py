positivo = 0
media = 0
for x in range(1,7):
    a = float(input())
    if a > 0:
        positivo +=1
        media = media + a

media = media /positivo
print("{} valores positivos".format(positivo))
print("{:.1f}".format(media))