cedulas = [100, 50, 20, 10, 5, 2, 1]
n = int(input("Informe um valor entre 0  e 1000000: "))

while n > 1000000:
    n = int(input("Informe um valor entre 0  e 1000000: "))

while n < 0:
    n = int(input("Informe um valor entre 0  e 1000000: "))

for x in cedulas:
    q_cedulas = int(n / x)
    print(f"{q_cedulas} nota(s) de R${x},00")
    n = n - (q_cedulas * x)
    continue