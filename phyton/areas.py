pi = 3.14159
valor = input().split(" ")
a,b,c = valor


a_tri = (a * c)/2
a_circ = pi * (c**2)
a_trap = ((a+b) * c)/2
a_quad = b**2
a_ret = a * b

print("TRIANGULO: %.3f" %a_tri)
print("CIRCULO: %.3f" %a_circ)
print("TRAPEZIO: %.3f" %a_trap)
print("QUADRADO: %.3f" %a_quad)
print("RETANGULO: %.3f" %a_ret)