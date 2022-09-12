from re import X


x = int(input("Distância percorrida (em Km):"))
y = float(input("Combustível gasto (em litros):"))

cons=(x/y)

print("%.3f" % cons, "km/l")