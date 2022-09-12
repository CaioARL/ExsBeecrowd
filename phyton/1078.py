n = int(input())

while (n >1000) and (n < 2):
    n = int(input())

a = 0
for x in range(1,11):
    a+=1
    r = a * n
    print("{} x {} = {}".format(a, n, r))