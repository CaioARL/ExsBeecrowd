s = float(input())
perc = [0.15, 0.12, 0.10, 0.07, 0.04]

if s >= 0 and s <= 400:
    reajuste = s * float(perc[0])
    print("Novo salario: {:.2f}".format(s + reajuste))
    print("Reajuste ganho: %.2f" %reajuste)
    print("Em percentual: 15 %")

if s >= 400.01 and s <= 800:
    reajuste = s * float(perc[1])
    print("Novo salario: {:.2f}".format(s + reajuste))
    print("Reajuste ganho: %.2f" %reajuste)
    print("Em percentual: 12 %")
    
if s >= 800.01 and s <= 1200:
    reajuste = s * float(perc[2])
    print("Novo salario: {:.2f}".format(s + reajuste))
    print("Reajuste ganho: %.2f" %reajuste)
    print("Em percentual: 10 %")

if s >= 1200.01 and s <= 2000:
    reajuste = s * float(perc[3])
    print("Novo salario: {:.2f}".format(s + reajuste))
    print("Reajuste ganho: %.2f" %reajuste)
    print("Em percentual: 7 %")

if s > 2000:
    reajuste = s * float(perc[4])
    print("Novo salario: {:.2f}".format(s + reajuste))
    print("Reajuste ganho: %.2f" %reajuste)
    print("Em percentual: 4 %")