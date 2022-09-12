N = int(input())

while 5 < N and N > 2000:
    N = int(input())

for x in range(1,N + 1):
    if x %2 ==0:
        print("{}^2 = {}".format(x,(x**2)))