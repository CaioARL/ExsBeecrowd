cedulas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
N = float(input())
 
while N > 1000000.00:
    N = float(input())
 
while N < 0:
    N = float(input())

print("NOTAS:")
for x in cedulas:
    q_cedulas = int(N / x)
    print(f"{q_cedulas} nota(s) de R$ {x}.00")
    N = float('%g' % (N - (q_cedulas * x)))

print(N)

print("MOEDAS:")
for x in moedas:
    q_moedas = int(N / x)
    print(f"{q_moedas} moeda(s) de R$ ""%.2f" % x)
    N = float('%g' % (N - (q_moedas * x)))

print(N)