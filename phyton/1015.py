import math

L1 = input().split(" ")
L2 = input().split(" ")

x1, y1 = L1
x2, y2 = L2

D = (((float(x2) - float (x1))**2) + ((float(y2) - float (y1))**2))
raiz = math.sqrt(D)
print ("%.4f" %raiz)