a = []

for x in range(100):
    n = float(input())
    a.append(n)
    if n <=10:
        print("A[{}] = {}".format(x,n))