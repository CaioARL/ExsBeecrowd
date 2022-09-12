h1,m1,h2,m2 = input().split(" ")

h1 = int(h1)
m1 = int(m1)
h2 = int(h2)
m2 = int(m2)

calc = ((h2*60) + m2) - ((h1*60) + m1)

if calc<=0:
    calc += 24*60

hora = int(calc / 60)
minutos = calc % 60

print(f"O JOGO DUROU {hora} HORA(S) E {minutos} MINUTO(S)")