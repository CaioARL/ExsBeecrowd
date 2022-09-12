n = int(input())

if n<1000 and n>=1:
    for x in range(1,n+1):
        print("{} {} {}".format(x,x**2,x**3))