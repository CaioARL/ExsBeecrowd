s = float(input())

if s >= 2000.01 and s<= 3000.00:
    c1 = s - 2000
    c2 = c1 * 0.08
    print("R$ {:.2f}".format(c2))

if s >=3000.01 and s <= 4500.00:
    c1 = s - 3000
    c2 = c1 * 0.18
    c3 = c2 + 80
    print("R$ {:.2f}".format(c3))

if s > 4500:
    c1 = s - 4500
    c2 = c1 * 0.28
    c3 = c2 + 270 + 80
    print("R$ {:.2f}".format(c3))

if s < 2000:
    print("Isento")