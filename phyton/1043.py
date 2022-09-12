a,b,c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)

if (b-c) < a and (b+c) > a:
    if (a-c) < b and (a+c) > a:
        if (a-b) < b and (a+b) > a:
            peri = a + b + c
            print("Perimetro = %.1f" %peri)
else:
    area = ((a + b) * c )/2
    print("Area = %.1f" %area)