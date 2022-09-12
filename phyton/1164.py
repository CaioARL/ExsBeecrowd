t = int(input())

for x in range(t):
    perf = 0
    n = int(input())
    for x in range(1, n):
        if n % x == 0:
            perf += x
    if perf == n:
        print("{} eh perfeito".format(n))
    else:
        print("{} nao eh perfeito".format(n))
