valor = input().split(" ")
cod, q = valor

c = [4.0, 4.50, 5.0, 2.0, 1.50]
cod = (int(cod) - 1)
v_cod = c[int(cod)]

conta = (int(q) * v_cod)

print(conta)