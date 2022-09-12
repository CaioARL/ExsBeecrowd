import math


ENTRADA = input().split(" ")
A,B,C = ENTRADA
A = float(A)
B = float(B)
C = float(C)

delta = (B**2) - (4*A*C)

if (delta > 0) and  (2 * A != 0):
    X = ((-B) + math.sqrt(delta))/(2*A)
    X1 = ((-B) - math.sqrt(delta))/(2*A)
    print("R1 = %.5F" %X )
    print("R2 = %.5F" %X1 )

else:
    print("Impossivel calcular")