valor1 = input().split(" ")
valor2 = input().split(" ")
p10, p11, p12 = valor1
p20, p21, p22 = valor2

vl_pg = ( int(p11) * float(p12) ) + ( int(p21)* float(p22) )
print("VALOR A PAGAR = R$ %.2f" %vl_pg)